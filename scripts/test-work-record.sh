#!/usr/bin/env bash
# Behavioral checks; all generated project data stays in repository-local tmp/.
set -euo pipefail
repository=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
helper=$repository/plugins/lusona/scripts/work-record.sh
mkdir -p "$repository/tmp"
scratch=$(mktemp -d "$repository/tmp/work-record-test.XXXXXX")
trap 'rm -rf -- "$scratch"' EXIT

equal() {
  [[ $1 == "$2" ]] || { printf 'Expected <%s>, got <%s>\n' "$2" "$1" >&2; exit 1; }
}
reject() {
  if bash "$helper" "$@" > "$scratch/rejected.out" 2>&1; then
    printf 'Unexpected success: %s\n' "$*" >&2
    exit 1
  fi
}

for pair in 01:01 07:01 08:02 14:02 15:03 21:03 22:04 28:04 29:05 30:05; do
  equal "$(bash "$helper" history-path "2026-09-${pair%:*}")" "docs/lusona/history/2026-09-week-${pair#*:}.md"
done
for pair in 2024-02-29:2024-02-week-05 2000-02-29:2000-02-week-05 2026-12-31:2026-12-week-05 2027-01-01:2027-01-week-01; do
  equal "$(bash "$helper" history-path "${pair%:*}")" "docs/lusona/history/${pair#*:}.md"
done
for invalid in '' 2026-02-29 1900-02-29 2026-04-31 2026-00-10 2026-13-10 2026-09-00 2026-09-31 0000-01-01 26-09-01 tomorrow; do
  reject history-path "$invalid"
done
equal "$(bash "$helper" slug '  JS/TS path aliases!  ')" 'js-ts-path-aliases'
equal "$(bash "$helper" slug $'Rust\n\nbackend')" 'rust-backend'
reject slug '!!!'
reject unknown
reject init-notes "$scratch" '../escape'
reject init-notes "$scratch" 'MixedCase'
reject init-history "$scratch/missing" 2026-09-10

project="$scratch/project with spaces"
mkdir -p "$project"
history=$(bash "$helper" init-history "$project" 2026-09-10)
equal "$history" "$project/docs/lusona/history/2026-09-week-02.md"
[[ -s $history ]]
# A relocated helper must use its bundled template, regardless of working directory.
bundle="$scratch/relocated plugin"
mkdir -p "$bundle/scripts" "$bundle/templates"
cp "$helper" "$bundle/scripts/work-record.sh"
cp "$repository/plugins/lusona/templates/history.md" "$bundle/templates/history.md"
printf '\nBundle-specific template content.\n' >> "$bundle/templates/history.md"
relocated_history=$(cd "$scratch" && bash "$bundle/scripts/work-record.sh" init-history "$project" 2026-09-15)
expected=$(cat "$bundle/templates/history.md")
expected=${expected//\{\{period\}\}/2026-09-week-03}
equal "$(cat "$relocated_history")" "$expected"
cp "$repository/plugins/lusona/templates/notes.md" "$bundle/templates/notes.md"
printf '\nBundle-specific notes content.\n' >> "$bundle/templates/notes.md"
relocated_notes=$(cd "$scratch" && bash "$bundle/scripts/work-record.sh" init-notes "$project" investigation-probe)
expected=$(cat "$bundle/templates/notes.md")
expected=${expected//\{\{slug\}\}/investigation-probe}
equal "$(cat "$relocated_notes")" "$expected"
printf 'Existing evidence\n' >> "$history"
cp "$history" "$scratch/history-before"
equal "$(bash "$helper" init-history "$project" 2026-09-14)" "$history"
cmp "$history" "$scratch/history-before"
notes=$(bash "$helper" init-notes "$project" rust-backend)
equal "$notes" "$project/docs/lusona/notes/rust-backend.md"
[[ -s $notes ]]
printf 'Keep this finding\n' >> "$notes"
cp "$notes" "$scratch/notes-before"
bash "$helper" init-notes "$project" rust-backend > /dev/null
cmp "$notes" "$scratch/notes-before"
ln -s "$notes" "$project/docs/lusona/notes/linked.md"
reject init-notes "$project" linked
mkdir "$project/docs/lusona/notes/directory.md"
reject init-notes "$project" directory

# Sequence lookup preserves combined-record and legacy split-record identities.
numbered="$scratch/numbered project"
mkdir "$numbered"
equal "$(bash "$helper" next-adr "$numbered")" '0001'
equal "$(bash "$helper" next-change "$numbered")" '0001'
[[ ! -e $numbered/docs ]]
mkdir -p "$numbered/docs/lusona/specs"
touch "$numbered/docs/lusona/specs/0003-combined.md"
equal "$(bash "$helper" next-change "$numbered")" '0004'
[[ ! -e $numbered/docs/lusona/plans ]]
mkdir -p "$numbered/docs/lusona/adr" "$numbered/docs/lusona/plans"
touch "$numbered/docs/lusona/adr/0001-first.md" "$numbered/docs/lusona/adr/0009-later.md"
touch "$numbered/docs/lusona/adr/README.md"
equal "$(bash "$helper" next-adr "$numbered")" '0010'
touch "$numbered/docs/lusona/adr/0009-conflict.md"
reject next-adr "$numbered"
rm "$numbered/docs/lusona/adr/0009-conflict.md"
touch "$numbered/docs/lusona/adr/not-numbered.md"
reject next-adr "$numbered"
rm "$numbered/docs/lusona/adr/not-numbered.md"
touch "$numbered/docs/lusona/adr/9999-last.md"
reject next-adr "$numbered"
touch "$numbered/docs/lusona/specs/legacy-change.md"
touch "$numbered/docs/lusona/specs/0042-shared.md" "$numbered/docs/lusona/plans/0042-shared.md"
touch "$numbered/docs/lusona/plans/0048-standalone.md"
equal "$(bash "$helper" next-change "$numbered")" '0049'
touch "$numbered/docs/lusona/specs/0048-conflict.md"
reject next-change "$numbered"
rm "$numbered/docs/lusona/specs/0048-conflict.md"
touch "$numbered/docs/lusona/specs/49-malformed.md"
reject next-change "$numbered"

# Date-based records need no sequence allocation and preserve legacy files.
cp "$numbered/docs/lusona/specs/0042-shared.md" "$scratch/legacy-before"
for kind in change adr; do
  directory=specs
  [[ $kind != adr ]] || directory=adr
  response=$(bash "$helper" "init-$kind" "$numbered" add-python-support 2026-09-26)
  record=$(python3 -c 'import json,sys; r=json.load(sys.stdin); assert r["status"] == "created"; print(r["path"])' <<< "$response")
  equal "$record" "$numbered/docs/lusona/$directory/20260926-add-python-support.md"
  [[ $(sed -n 's/^Created: //p' "$record") == 2026-09-26 ]]
  [[ $(sed -n 's/^Updated: //p' "$record") == 2026-09-26 ]]
  printf 'Preserve this evidence\n' >> "$record"
  cp "$record" "$scratch/dated-before"
  conflict_code=0
  bash "$helper" "init-$kind" "$numbered" add-python-support 2026-09-26 > "$scratch/conflict.json" || conflict_code=$?
  equal "$conflict_code" 3
  python3 -c 'import json,sys; r=json.load(open(sys.argv[1])); assert r["status"] == "conflict" and r["path"] == sys.argv[2]' "$scratch/conflict.json" "$record"
  cmp "$record" "$scratch/dated-before"
  reject "init-$kind" "$numbered" ../escape 2026-09-26
  python3 -c 'import json,sys; r=json.load(open(sys.argv[1])); assert r["status"] == "error" and r["message"]' "$scratch/rejected.out"
  reject "init-$kind" "$numbered" add-python-support 2026-02-29
  ln -s "$record" "$numbered/docs/lusona/$directory/20260926-linked.md"
  reject "init-$kind" "$numbered" linked 2026-09-26
  bash "$helper" "init-$kind" "$numbered" another-function 2026-09-26 > /dev/null &
  first=$!
  bash "$helper" "init-$kind" "$numbered" independent-function 2026-09-26 > /dev/null &
  second=$!
  wait "$first"
  wait "$second"
  # Racing creators of one path must yield exactly one success.
  (if bash "$helper" "init-$kind" "$numbered" same-function 2026-09-26 > /dev/null 2>&1; then echo yes; else echo no; fi) > "$scratch/race-one" &
  first=$!
  (if bash "$helper" "init-$kind" "$numbered" same-function 2026-09-26 > /dev/null 2>&1; then echo yes; else echo no; fi) > "$scratch/race-two" &
  second=$!
  wait "$first"
  wait "$second"
  equal "$(sort "$scratch/race-one" "$scratch/race-two")" $'no\nyes'
done
cmp "$numbered/docs/lusona/specs/0042-shared.md" "$scratch/legacy-before"
# JSON responses preserve quoted, escaped, and multiline project paths.
unusual="$scratch/"$'quoted"-backslash\\-newline\nproject'
mkdir "$unusual"
response=$(bash "$helper" init-change "$unusual" json-path 2026-09-26)
python3 -c 'import json,sys; r=json.load(sys.stdin); assert r["path"] == sys.argv[1]' "$unusual/docs/lusona/specs/20260926-json-path.md" <<< "$response"
# Defaults use the local creation date and relocated templates stay self-contained.
cp "$repository/plugins/lusona/templates/spec.md" "$bundle/templates/spec.md"
printf '\nBundle-specific spec content.\n' >> "$bundle/templates/spec.md"
response=$(bash "$bundle/scripts/work-record.sh" init-change "$project" default-date)
record=$(python3 -c 'import json,sys; print(json.load(sys.stdin)["path"])' <<< "$response")
equal "$record" "$project/docs/lusona/specs/$(date +%Y%m%d)-default-date.md"
[[ $(tail -n 1 "$record") == 'Bundle-specific spec content.' ]]
mkdir "$project/docs/lusona/specs/20260926-existing-directory.md"
reject init-change "$project" existing-directory 2026-09-26
python3 -c 'import json,sys; assert json.load(open(sys.argv[1]))["status"] == "conflict"' "$scratch/rejected.out"
reject init-change "$scratch/missing-project" valid-slug
python3 -c 'import json,sys; assert json.load(open(sys.argv[1]))["status"] == "error"' "$scratch/rejected.out"

# A filesystem write failure is an error, not an existing-record conflict.
python3 - "$helper" "$project" <<'PYTEST'
import json, resource, signal, subprocess, sys

def restrict_writes():
    resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    signal.signal(signal.SIGXFSZ, signal.SIG_IGN)

result = subprocess.run(
    ["bash", sys.argv[1], "init-change", sys.argv[2], "write-failure", "2026-09-26"],
    capture_output=True, text=True, preexec_fn=restrict_writes)
assert result.returncode == 1, result
assert json.loads(result.stdout)["status"] == "error", result
PYTEST

# Legacy lookup still works alongside valid dated records.
rm "$numbered/docs/lusona/specs/49-malformed.md" "$numbered/docs/lusona/adr/9999-last.md"
rm "$numbered/docs/lusona/specs/20260926-linked.md" "$numbered/docs/lusona/adr/20260926-linked.md"
equal "$(bash "$helper" next-change "$numbered")" '0049'
equal "$(bash "$helper" next-adr "$numbered")" '0010'

# Header stamping fills templates, preserves Created and body, and rejects stale dates.
for kind in spec adr; do
  record="$scratch/$kind.md"
  cp "$repository/plugins/lusona/templates/$kind.md" "$record"
  bash "$helper" stamp-header "$record" 2026-09-10 > /dev/null
  [[ $(sed -n 's/^Created: //p' "$record") == 2026-09-10 ]]
  bash "$helper" stamp-header "$record" 2026-09-12 > /dev/null
  [[ $(sed -n 's/^Created: //p' "$record") == 2026-09-10 ]]
  [[ $(sed -n 's/^Updated: //p' "$record") == 2026-09-12 ]]
  cp "$record" "$scratch/header-before"
  reject stamp-header "$record" 2026-09-11
  cmp "$record" "$scratch/header-before"
done
record="$scratch/body.md"
printf '# Spec 0042: Example\n\nCreated: <YYYY-MM-DD>\nUpdated: <YYYY-MM-DD>\n\n## Body\nLiteral $HOME and `code`.\n\n' > "$record"
tail -n 4 "$record" > "$scratch/body-before"
bash "$helper" stamp-header "$record" 2026-09-10 > /dev/null
tail -n 4 "$record" > "$scratch/body-after"
cmp "$scratch/body-before" "$scratch/body-after"
cp "$record" "$scratch/header-before"
reject stamp-header "$record" 2026-02-29
cmp "$record" "$scratch/header-before"
printf 'Updated: 2026-09-10\n' >> "$record"
cp "$record" "$scratch/header-before"
reject stamp-header "$record" 2026-09-12
cmp "$record" "$scratch/header-before"
reject stamp-header "$scratch/missing.md" 2026-09-12
ln -s "$record" "$scratch/linked-header.md"
reject stamp-header "$scratch/linked-header.md" 2026-09-12
printf '# Plan 0042: Example\nCreated: 2026-09-10\nUpdated: 2026-09-10\n\nNo final newline' > "$scratch/no-newline.md"
printf '# Plan 0042: Example\nCreated: 2026-09-10\nUpdated: 2026-09-12\n\nNo final newline' > "$scratch/no-newline-expected.md"
bash "$helper" stamp-header "$scratch/no-newline.md" 2026-09-12 > /dev/null
cmp "$scratch/no-newline.md" "$scratch/no-newline-expected.md"
printf 'Work-record behavioral checks passed.\n'
