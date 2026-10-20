"""Validate and reproducibly package the canonical skill; standard library only."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'secure-product-development'


def validate(skill: Path) -> list[Path]:
    entry = skill / 'SKILL.md'
    text = entry.read_text(encoding='utf-8')
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        raise ValueError('SKILL.md requires YAML frontmatter')
    front = text.split('---', 2)[1]
    if not re.search(r'^name: ' + re.escape(NAME) + r'$', front, re.M):
        raise ValueError('Skill name must match its directory')
    if not re.search(r'^description: .+', front, re.M):
        raise ValueError('Missing description')
    files = sorted(p for p in skill.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in skill.rglob('*')):
        raise ValueError('Symlinks are not allowed in the package')
    if any(p.suffix != '.md' for p in files):
        raise ValueError('Only reviewed Markdown resources belong in this skill')
    root = skill.resolve()
    for source in files:
        for link in re.findall(r'\]\(([^)]+)\)', source.read_text(encoding='utf-8')):
            if re.match(r'https?://', link) or link.startswith('#'):
                continue
            target = (source.parent / link.split('#', 1)[0]).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                raise ValueError(f'Unsafe or missing reference: {source.name}: {link}')
    return files


def build(skill: Path, output: Path, license_path: Path) -> dict:
    files = validate(skill)
    output.parent.mkdir(parents=True, exist_ok=True)
    entries = [(f'{NAME}/{p.relative_to(skill).as_posix()}', p.read_bytes()) for p in files]
    entries.append((f'{NAME}/LICENSE', license_path.read_bytes()))
    # Stored entries avoid zlib-version variation. Explicit Unix metadata avoids
    # ZipInfo's platform-dependent creator byte in the central directory.
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, content in sorted(entries):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    return {'file': output.name, 'entries': len(entries),
            'sha256': hashlib.sha256(output.read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist' / f'{NAME}.skill')
    options = parser.parse_args()
    print(json.dumps(build(ROOT / 'skills' / NAME, options.output, ROOT / 'LICENSE'), indent=2))
