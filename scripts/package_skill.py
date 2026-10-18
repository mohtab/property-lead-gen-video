#!/usr/bin/env python3
"""Build a portable skill ZIP. Uses only Python's standard library."""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = 'property-lead-gen-video'
SOURCE = ROOT / 'skills' / NAME
OUTPUT = ROOT / 'dist' / f'{NAME}.zip'


def main():
    manifest = SOURCE / 'SKILL.md'
    text = manifest.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError('SKILL.md must begin with YAML frontmatter')
    if not re.search(rf'^name:\s*{re.escape(NAME)}\s*$', parts[1], re.M):
        raise ValueError('The frontmatter name must match the skill folder')
    if not re.search(r'^description:\s*\S.+$', parts[1], re.M):
        raise ValueError('Missing one-line description')
    files = sorted(p for p in SOURCE.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in SOURCE.rglob('*')):
        raise ValueError('Package files must not be symlinks')
    if any(part.startswith('.') or part == '__pycache__'
           for p in files for part in p.relative_to(SOURCE).parts):
        raise ValueError('Unexpected hidden/cache file in skill folder')
    for p in files:
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                resolved = (p.parent / target.split('#')[0]).resolve()
                if not resolved.is_relative_to(SOURCE.resolve()) or not resolved.is_file():
                    raise ValueError(f'Broken or external local reference in {p.name}: {target}')
    OUTPUT.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            entry = zipfile.ZipInfo(f'{NAME}/{p.relative_to(SOURCE).as_posix()}',
                                   date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, p.read_bytes())
    with zipfile.ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP integrity check failed')
        expected = {f'{NAME}/{p.relative_to(SOURCE).as_posix()}' for p in files}
        if set(archive.namelist()) != expected:
            raise ValueError('ZIP contents do not match the skill source')
        for p in files:
            if archive.read(f'{NAME}/{p.relative_to(SOURCE).as_posix()}') != p.read_bytes():
                raise ValueError('ZIP bytes differ from source')
    print(f'Validated {len(files)} files; built {OUTPUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
