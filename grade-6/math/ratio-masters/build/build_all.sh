#!/usr/bin/env bash
# Rebuild every example from the generators, then export production files.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
for g in v01 v02 v02f v03 v04 v05 v06 v07 v08 v08t v09 v01f v10; do python3 "$HERE/generators/$g.py" "$TMP" >/dev/null; done
python3 "$HERE/export.py" "$TMP" "$HERE/.."
rm -rf "$TMP"
