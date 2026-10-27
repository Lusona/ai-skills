#!/usr/bin/env bash
set -euo pipefail
export LC_ALL=C

usage() {
  printf '%s\n' 'See the bundled work-record reference for commands and arguments'
}

json_string() {
  local value=$1 character index
  printf '"'
  for ((index=0; index<${#value}; index++)); do
    character=${value:index:1}
    case $character in
      '"') printf '\\"' ;;
      '\') printf '\\\\' ;;
      *)
        if [[ $character < ' ' ]]; then
          printf '\\u%04x' "'$character"
        else
          printf '%s' "$character"
        fi ;;
    esac
  done
  printf '"'
}

record_response() {
  printf '{"status":'
  json_string "$1"
  printf ',"path":'
  json_string "$2"
  printf ',"message":'
  json_string "$3"
  printf '}\n'
}

fail() {
  if [[ ${record_json:-0} == 1 ]]; then
    record_response error "${record_path:-}" "$*"
  else
    printf 'work-record: %s\n' "$*" >&2
  fi
  exit 1
}

read_template() {
  local resource_root
  resource_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
  cat "$resource_root/templates/$1.md"
}

validate_date() {
  local record_date=$1 year month day days
  [[ $record_date =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || fail 'Date must be YYYY-MM-DD'
  year=$((10#${record_date:0:4}))
  month=$((10#${record_date:5:2}))
  day=$((10#${record_date:8:2}))
  (( year >= 1 && month >= 1 && month <= 12 )) || fail "Invalid date: $record_date"
  case $month in
    4|6|9|11) days=30 ;;
    2)
      days=28
      if (( year % 400 == 0 || (year % 4 == 0 && year % 100 != 0) )); then days=29; fi ;;
    *) days=31 ;;
  esac
  (( day >= 1 && day <= days )) || fail "Invalid date: $record_date"
}

history_path() {
  local record_date=${1-$(date +%F)} year month day week
  validate_date "$record_date"
  year=$((10#${record_date:0:4}))
  month=$((10#${record_date:5:2}))
  day=$((10#${record_date:8:2}))
  week=$(((day - 1) / 7 + 1))
  printf 'docs/lusona/history/%04d-%02d-week-%02d.md\n' "$year" "$month" "$week"
}

project_root() {
  [[ -d $1 ]] || fail "Project root is not a directory: $1"
  (cd -- "$1" && pwd -P)
}

next_sequence() {
  local kind=$1 root directory file name number previous maximum=0
  local -a directories seen_names=() seen_directories=()
  root=$(project_root "$2")
  if [[ $kind == adr ]]; then
    directories=("$root/docs/lusona/adr")
  else
    directories=("$root/docs/lusona/specs" "$root/docs/lusona/plans")
  fi
  for directory in "${directories[@]}"; do
    [[ ! -e $directory || -d $directory ]] || fail "Not a directory: $directory"
    for file in "$directory"/*.md; do
      [[ -e $file || -L $file ]] || continue
      name=${file##*/}
      [[ $name != README.md ]] || continue
      if [[ $name =~ ^[0-9]{8}-[a-z0-9]+(-[a-z0-9]+)*\.md$ ]]; then
        validate_date "${name:0:4}-${name:4:2}-${name:6:2}"
        [[ -f $file && ! -L $file ]] || fail "Not a regular non-symlink record: $file"
        continue
      fi
      if [[ ! $name =~ ^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$ ]]; then
        if [[ $kind == change && ! $name =~ ^[0-9] ]]; then continue; fi
        fail "Malformed $kind filename: $file"
      fi
      [[ -f $file && ! -L $file ]] || fail "Not a regular non-symlink record: $file"
      number=$((10#${name:0:4}))
      (( number > 0 )) || fail "Sequence must start at 0001: $file"
      if [[ $kind == change && $name =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}(-|\.md$) ]]; then
        fail "Date-prefixed change filename is not a sequence: $file"
      fi
      previous=${seen_names[number]-}
      if [[ -n $previous ]]; then
        [[ $kind == change && $previous == "$name" && ${seen_directories[number]} != "$directory" ]] ||
          fail "Duplicate sequence ${name:0:4}: $previous and $file"
      fi
      seen_names[number]=$name
      seen_directories[number]=$directory
      if (( number > maximum )); then maximum=$number; fi
    done
  done
  (( maximum < 9999 )) || fail 'Sequence exhausted at 9999'
  printf '%04d\n' "$((maximum + 1))"
}

create_record() {
  local kind=$1 root slug=$3 record_date=${4-$(date +%F)} directory template identifier destination result=0
  [[ -d $2 ]] || fail "Project root is not a directory: $2"
  root=$(cd -- "$2" 2>/dev/null && pwd -P) || fail "Could not resolve project root: $2"
  [[ $slug =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || fail 'Slug must contain lowercase ASCII letters/digits separated by single hyphens'
  validate_date "$record_date"
  identifier="${record_date//-/}-$slug"
  if [[ $kind == change ]]; then
    directory=specs
    template=$(read_template spec) || fail 'Could not read spec template'
    template=${template//<change-id>/$identifier}
  else
    directory=adr
    template=$(read_template adr) || fail 'Could not read ADR template'
    template=${template//<decision-id>/$identifier}
  fi
  template=${template//<YYYY-MM-DD>/$record_date}
  destination="$root/docs/lusona/$directory/$identifier.md"
  record_path=$destination
  if [[ -e $destination || -L $destination ]]; then
    record_response conflict "$destination" 'Path exists; inspect the record or choose a more specific functional slug'
    exit 3
  fi
  mkdir -p -- "${destination%/*}" 2>/dev/null || fail "Could not create record directory: ${destination%/*}"
  (
    set -o noclobber
    exec 3> "$destination" || exit 3
    trap 'rm -f -- "$destination"' EXIT
    printf '%s\n' "$template" >&3 || exit 1
    trap - EXIT
  ) 2>/dev/null || result=$?
  if [[ $result -eq 3 ]]; then
    if [[ -e $destination || -L $destination ]]; then
      record_response conflict "$destination" 'Path exists; inspect the record or choose a more specific functional slug'
      exit 3
    fi
    fail "Could not create: $destination"
  elif [[ $result -ne 0 ]]; then
    fail "Could not write record; inspect and remove any incomplete output before retrying: $destination"
  fi
  record_response created "$destination" 'Record created; fill the title and relevant template sections'
}

stamp_header() (
  local file=$1 record_date=${2-$(date +%F)} line newline
  local created='' updated='' created_count=0 updated_count=0 temporary
  [[ -f $file && ! -L $file ]] || fail "Not a regular non-symlink file: $file"
  validate_date "$record_date"
  while IFS= read -r line || [[ -n $line ]]; do
    case $line in
      Created:*) created_count=$((created_count + 1)); created=${line#Created: } ;;
      Updated:*) updated_count=$((updated_count + 1)); updated=${line#Updated: } ;;
    esac
  done < "$file"
  [[ $created_count -eq 1 && $updated_count -eq 1 ]] || fail 'Header requires exactly one Created: and one Updated: field'
  if [[ $created == '<YYYY-MM-DD>' ]]; then created=$record_date; else validate_date "$created"; fi
  [[ ! $record_date < $created ]] || fail 'Stamp date precedes Created date'
  if [[ $updated != '<YYYY-MM-DD>' ]]; then
    validate_date "$updated"
    [[ ! $updated < $created ]] || fail 'Updated date precedes Created date'
    [[ ! $record_date < $updated ]] || fail 'Stamp date precedes current Updated date'
  fi
  temporary=$(mktemp "${file}.stamp.XXXXXX") || fail 'Could not create temporary header file'
  trap 'rm -f -- "$temporary"' EXIT
  cp -p -- "$file" "$temporary"
  while :; do
    newline=''
    if IFS= read -r line; then newline=$'\n'; elif [[ -z $line ]]; then break; fi
    case $line in
      Created:*) line="Created: $created" ;;
      Updated:*) line="Updated: $record_date" ;;
    esac
    printf '%s%s' "$line" "$newline"
    [[ -n $newline ]] || break
  done < "$file" > "$temporary"
  mv -- "$temporary" "$file"
)

initialize() {
  local destination=$1 heading=$2
  [[ ! -L $destination ]] || fail "Refusing symlink: $destination"
  if [[ -e $destination ]]; then
    [[ -f $destination ]] || fail "Not a regular file: $destination"
  else
    mkdir -p -- "${destination%/*}"
    (set -o noclobber; printf '%s\n' "$heading" > "$destination") || fail "Could not create: $destination"
  fi
  printf '%s\n' "$destination"
}

[[ $# -ge 1 ]] || { usage >&2; exit 1; }
command_name=$1
shift
case $command_name in
  -h|--help|help) usage ;;
  slug)
    [[ $# -eq 1 ]] || fail 'slug requires one quoted title'
    slug=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9][^a-z0-9]*/-/g; s/^-//; s/-$//')
    slug=$(printf '%s' "$slug" | tr '\n' '-' | sed 's/--*/-/g; s/^-//; s/-$//')
    [[ -n $slug ]] || fail 'Title must contain an ASCII letter or digit'
    printf '%s\n' "$slug"
    ;;
  history-path)
    [[ $# -le 1 ]] || fail 'history-path accepts at most one date'
    history_path "$@"
    ;;
  init-history)
    [[ $# -ge 1 && $# -le 2 ]] || fail 'init-history requires a project root and optional date'
    relative=$(history_path "${@:2}")
    root=$(project_root "$1")
    period=${relative##*/}
    template=$(read_template history)
    initialize "$root/$relative" "${template//\{\{period\}\}/${period%.md}}"
    ;;
  init-notes)
    [[ $# -eq 2 ]] || fail 'init-notes requires a project root and existing item slug'
    [[ $2 =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || fail 'Slug must contain lowercase ASCII letters/digits separated by single hyphens'
    root=$(project_root "$1")
    template=$(read_template notes)
    initialize "$root/docs/lusona/notes/$2.md" "${template//\{\{slug\}\}/$2}"
    ;;
  init-change|init-adr)
    record_json=1
    [[ $# -ge 2 && $# -le 3 ]] || fail "$command_name requires a project root, functional slug, and optional date"
    create_record "${command_name#init-}" "$@"
    ;;
  next-adr|next-change)
    [[ $# -eq 1 ]] || fail "$command_name requires one project root"
    next_sequence "${command_name#next-}" "$1"
    ;;
  stamp-header)
    [[ $# -ge 1 && $# -le 2 ]] || fail 'stamp-header requires a file and optional date'
    stamp_header "$@"
    ;;
  *) usage >&2; fail "Unknown command: $command_name" ;;
esac
