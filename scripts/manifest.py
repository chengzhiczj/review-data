"""Maintain checksums of immutable release inputs and analysis source code."""
from pathlib import Path
import argparse

from .common import ROOT, sha256


def write_manifest(root=ROOT):
    root = Path(root)
    lines = []
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if not path.is_file() or relative.parts[0] == 'results' or '__pycache__' in relative.parts:
            continue
        if path.name == 'MANIFEST.sha256' or path.suffix in ['.pyc', '.zip']:
            continue
        lines.append(sha256(path) + '  ' + relative.as_posix())
    (root / 'MANIFEST.sha256').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return len(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', required=True)
    parser.parse_args()
    print('Recorded input/source checksums:', write_manifest())
