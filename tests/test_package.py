from pathlib import Path
import importlib.util
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('packager', ROOT / 'tools/package_skill.py')
packager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packager)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / packager.NAME
        self.skill.mkdir()
        self.entry = self.skill / 'SKILL.md'
        self.entry.write_text('---\nname: secure-product-development\ndescription: Secure coding\n---\n', encoding='utf-8')
        self.license = self.root / 'LICENSE'
        self.license.write_text('Test license', encoding='utf-8')

    def test_real_package_is_deterministic_and_contains_license(self):
        one, two = self.root / 'one.skill', self.root / 'two.skill'
        actual = ROOT / 'skills' / packager.NAME
        first = packager.build(actual, one, ROOT / 'LICENSE')
        second = packager.build(actual, two, ROOT / 'LICENSE')
        self.assertEqual(first['sha256'], second['sha256'])
        with zipfile.ZipFile(one) as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn(f'{packager.NAME}/LICENSE', archive.namelist())
            self.assertTrue(all(n.startswith(f'{packager.NAME}/') and '..' not in n for n in archive.namelist()))
            self.assertEqual(len(archive.namelist()), 6)

    def test_missing_reference_rejected(self):
        with self.entry.open('a', encoding='utf-8') as handle:
            handle.write('[missing](references/missing.md)')
        with self.assertRaisesRegex(ValueError, 'missing reference'):
            packager.validate(self.skill)

    def test_reference_cannot_escape_skill(self):
        (self.root / 'private.md').write_text('Private', encoding='utf-8')
        with self.entry.open('a', encoding='utf-8') as handle:
            handle.write('[private](../private.md)')
        with self.assertRaisesRegex(ValueError, 'Unsafe'):
            packager.validate(self.skill)

    def test_executable_resource_rejected(self):
        (self.skill / 'run.ps1').write_text('throw', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Only reviewed Markdown'):
            packager.validate(self.skill)

    def test_creator_platform_does_not_change_archive(self):
        original = zipfile.ZipInfo
        outputs = []
        for platform in (0, 3):
            class PlatformZipInfo(original):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.create_system = platform
            output = self.root / f'platform-{platform}.skill'
            with mock.patch.object(packager.zipfile, 'ZipInfo', PlatformZipInfo):
                packager.build(self.skill, output, self.license)
            outputs.append(output.read_bytes())
            with zipfile.ZipFile(output) as archive:
                for entry in archive.infolist():
                    self.assertEqual(entry.create_system, 3)
                    self.assertEqual(entry.compress_type, zipfile.ZIP_STORED)
        self.assertEqual(outputs[0], outputs[1])


if __name__ == '__main__':
    unittest.main()
