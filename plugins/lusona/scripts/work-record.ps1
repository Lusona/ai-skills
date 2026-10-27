# Naming and initialization for consuming-project work records.
# Compatible with Windows PowerShell 5.1 and PowerShell 7; no external tools.
$ErrorActionPreference = 'Stop'
$script:recordJson = $false
$script:recordPath = ''
$script:utf8 = New-Object Text.UTF8Encoding($false)
[Console]::OutputEncoding = $script:utf8
$arguments = @($args)

function Show-Usage {
    Write-Output @'
Usage: powershell -NoProfile -File work-record.ps1 COMMAND ARGS
  slug TITLE                         Print a lowercase ASCII change slug.
  history-path [YYYY-MM-DD]           Print the project-relative history path.
  init-history PROJECT_ROOT [DATE]    Create a weekly history file if absent.
  init-notes PROJECT_ROOT SLUG        Create an item's notes file if absent.
  init-change PROJECT_ROOT SLUG [DATE] Create a new YYYYMMDD-slug spec.
  init-adr PROJECT_ROOT SLUG [DATE]    Create a new YYYYMMDD-slug ADR.
  next-adr PROJECT_ROOT               Legacy: print the next four-digit ADR number.
  next-change PROJECT_ROOT            Legacy: print the next change number, including plans.
  stamp-header FILE [DATE]            Initialize Created and update Updated.

DATE is YYYY-MM-DD, defaulting to today in the local timezone.
Weeks are month-local: 01 = days 1-7, 02 = 8-14, ... 05 = 29-end.
init-change and init-adr print JSON status/path/message: created (exit 0), conflict
(exit 3), or error (exit 1). They reject existing paths, including symlinks.
init-history and init-notes print the absolute native path and preserve existing regular files.
Reuse an item's existing slug; initialization never overwrites or merges records.
New specs and ADRs use the creation date and a functional slug; no counter is shared.
Legacy sequence commands are read-only, ignore dated records, and reserve nothing.
Legacy numbered filenames use NNNN-lowercase-slug.md; README.md is ignored.
Change scans ignore legacy filenames unless they begin with a digit.
Matching legacy spec/plan basenames share a number; conflicting slugs are rejected.
Header stamping requires exactly one Created: and Updated: field, each containing
a valid date or <YYYY-MM-DD>. Existing Created dates never change.
'@
}

function Write-RecordResponse([string]$status, [string]$path, [string]$message) {
    $response = [ordered]@{ status = $status; path = $path; message = $message }
    Write-Output ($response | ConvertTo-Json -Compress)
}
function Require-Count([int]$minimum, [int]$maximum, [string]$message) {
    if ($script:operands.Count -lt $minimum -or $script:operands.Count -gt $maximum) { throw $message }
}
function Get-RecordDate([string]$date) {
    if ($date -cnotmatch '^[0-9]{4}-[0-9]{2}-[0-9]{2}$') { throw 'Date must be YYYY-MM-DD.' }
    $parsed = [datetime]::MinValue
    if (-not [datetime]::TryParseExact($date, 'yyyy-MM-dd', [Globalization.CultureInfo]::InvariantCulture,
            [Globalization.DateTimeStyles]::None, [ref]$parsed)) { throw "Invalid date: $date" }
    return $parsed
}
function Get-DateArgument([int]$index) {
    if ($script:operands.Count -gt $index) { return $script:operands[$index] }
    return [datetime]::Now.ToString('yyyy-MM-dd', [Globalization.CultureInfo]::InvariantCulture)
}
function Assert-Slug([string]$slug) {
    if ($slug -cnotmatch '^[a-z0-9]+(-[a-z0-9]+)*$') {
        throw 'Slug must contain lowercase ASCII letters/digits separated by single hyphens.'
    }
}
function Get-ProjectRoot([string]$path) {
    # Resolve relative paths against PowerShell's location, which can differ from .NET's cwd.
    $item = Get-ExistingItem $path
    if ($null -eq $item -or -not $item.PSIsContainer -or $item.PSProvider.Name -ne 'FileSystem') {
        throw "Project root is not a directory: $path"
    }
    return $item.FullName
}
function Get-ExistingItem([string]$path) {
    # Get-Item also sees dangling links, which File.Exists/Test-Path can miss.
    return Get-Item -LiteralPath $path -Force -ErrorAction SilentlyContinue
}
function Test-Link($item) {
    return (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0)
}
function Assert-Regular($item, [string]$path) {
    if ($null -eq $item -or $item.PSIsContainer -or (Test-Link $item)) {
        throw "Not a regular non-symlink file: $path"
    }
}
function Read-Template([string]$name) {
    $resourceRoot = Split-Path -Parent $PSScriptRoot
    $path = Join-Path $resourceRoot "templates/$name.md"
    try { return [IO.File]::ReadAllText($path).TrimEnd([char]10) + "`n" }
    catch { throw "Could not read $name template." }
}
function Get-HistoryPath([string]$date) {
    $parsed = Get-RecordDate $date
    $week = [int][Math]::Floor(($parsed.Day - 1) / 7) + 1
    return 'docs/lusona/history/{0}-week-{1:00}.md' -f $date.Substring(0, 7), $week
}
function Write-NewFile([string]$path, [string]$content) {
    # CreateNew is the atomic ownership boundary; FileShare.None prevents competing writers.
    try {
        $stream = New-Object IO.FileStream($path, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
    } catch {
        # Windows can report an existing directory as UnauthorizedAccessException.
        # Mark only exclusive-open failures, never failures writing our own new file.
        $_.Exception.GetBaseException().Data['WorkRecordExclusiveOpenFailed'] = $true
        throw
    }
    try {
        $bytes = $script:utf8.GetBytes($content)
        $stream.Write($bytes, 0, $bytes.Length)
        $stream.Flush()
    } catch {
        $stream.Dispose()
        [IO.File]::Delete($path)
        throw "Could not write record: $path"
    } finally { $stream.Dispose() }
}
function Initialize-File([string]$path, [string]$content) {
    $item = Get-ExistingItem $path
    if ($null -ne $item) {
        Assert-Regular $item $path
    } else {
        [IO.Directory]::CreateDirectory((Split-Path -Parent $path)) | Out-Null
        Write-NewFile $path $content
    }
    Write-Output $path
}
function Create-Record([string]$kind, [string]$rootArgument, [string]$slug, [string]$date) {
    $root = Get-ProjectRoot $rootArgument
    Assert-Slug $slug
    $null = Get-RecordDate $date
    $identifier = $date.Replace('-', '') + '-' + $slug
    if ($kind -ceq 'change') {
        $directory = 'specs'
        $template = (Read-Template 'spec').Replace('<change-id>', $identifier)
    } else {
        $directory = 'adr'
        $template = (Read-Template 'adr').Replace('<decision-id>', $identifier)
    }
    $template = $template.Replace('<YYYY-MM-DD>', $date)
    $destination = Join-Path $root "docs/lusona/$directory/$identifier.md"
    $script:recordPath = $destination
    $conflictMessage = 'Path exists; inspect the record or choose a more specific functional slug.'
    if ($null -ne (Get-ExistingItem $destination)) {
        Write-RecordResponse 'conflict' $destination $conflictMessage
        exit 3
    }
    [IO.Directory]::CreateDirectory((Split-Path -Parent $destination)) | Out-Null
    try { Write-NewFile $destination $template }
    catch {
        # Only a failed exclusive open with an existing destination is a conflict.
        # Write-NewFile removes its own incomplete file after a write failure.
        if ($_.Exception.GetBaseException().Data['WorkRecordExclusiveOpenFailed'] -eq $true -and
                $null -ne (Get-ExistingItem $destination)) {
            Write-RecordResponse 'conflict' $destination $conflictMessage
            exit 3
        }
        throw
    }
    Write-RecordResponse 'created' $destination 'Record created; fill the title and relevant template sections.'
}
function Get-NextSequence([string]$kind, [string]$rootArgument) {
    $root = Get-ProjectRoot $rootArgument
    $directories = if ($kind -ceq 'adr') { @('adr') } else { @('specs', 'plans') }
    $seen = @{}
    $maximum = 0
    foreach ($name in $directories) {
        $directory = Join-Path $root "docs/lusona/$name"
        $item = Get-ExistingItem $directory
        if ($null -eq $item) { continue }
        if (-not $item.PSIsContainer) { throw "Not a directory: $directory" }
        foreach ($file in (Get-ChildItem -LiteralPath $directory -Force)) {
            $filename = $file.Name
            if (-not $filename.EndsWith('.md', [StringComparison]::Ordinal) -or $filename -ceq 'README.md') { continue }
            if ($filename -cmatch '^[0-9]{8}-[a-z0-9]+(-[a-z0-9]+)*\.md$') {
                $date = $filename.Substring(0, 4) + '-' + $filename.Substring(4, 2) + '-' + $filename.Substring(6, 2)
                $null = Get-RecordDate $date
                Assert-Regular $file $file.FullName
                continue
            }
            if ($filename -cnotmatch '^[0-9]{4}-[a-z0-9]+(-[a-z0-9]+)*\.md$') {
                if ($kind -ceq 'change' -and $filename -cnotmatch '^[0-9]') { continue }
                throw "Malformed $kind filename: $($file.FullName)"
            }
            Assert-Regular $file $file.FullName
            $number = [int]::Parse($filename.Substring(0, 4), [Globalization.CultureInfo]::InvariantCulture)
            if ($number -eq 0) { throw "Sequence must start at 0001: $($file.FullName)" }
            if ($kind -ceq 'change' -and $filename -cmatch '^[0-9]{4}-[0-9]{2}-[0-9]{2}(-|\.md$)') {
                throw "Date-prefixed change filename is not a sequence: $($file.FullName)"
            }
            if ($seen.ContainsKey($number)) {
                $previous = $seen[$number]
                if (-not ($kind -ceq 'change' -and $previous.Name -ceq $filename -and $previous.Directory -cne $directory)) {
                    throw "Duplicate sequence $($filename.Substring(0, 4)): $($previous.Name) and $($file.FullName)"
                }
            }
            $seen[$number] = @{ Name = $filename; Directory = $directory }
            if ($number -gt $maximum) { $maximum = $number }
        }
    }
    if ($maximum -ge 9999) { throw 'Sequence exhausted at 9999.' }
    Write-Output ($maximum + 1).ToString('0000', [Globalization.CultureInfo]::InvariantCulture)
}
function Stamp-Header([string]$pathArgument, [string]$date) {
    $item = Get-ExistingItem $pathArgument
    Assert-Regular $item $pathArgument
    $path = $item.FullName
    $null = Get-RecordDate $date
    # A one-byte encoding preserves UTF-8/BOMs and all body bytes without transcoding.
    $encoding = [Text.Encoding]::GetEncoding(28591)
    $content = $encoding.GetString([IO.File]::ReadAllBytes($path))
    $createdFields = [regex]::Matches($content, '(?m)^Created:[^\r\n]*')
    $updatedFields = [regex]::Matches($content, '(?m)^Updated:[^\r\n]*')
    if ($createdFields.Count -ne 1 -or $updatedFields.Count -ne 1) {
        throw 'Header requires exactly one Created: and one Updated: field.'
    }
    $created = $createdFields[0].Value -creplace '^Created: ', ''
    $updated = $updatedFields[0].Value -creplace '^Updated: ', ''
    if ($created -ceq '<YYYY-MM-DD>') { $created = $date } else { $null = Get-RecordDate $created }
    if ([string]::CompareOrdinal($date, $created) -lt 0) { throw 'Stamp date precedes Created date.' }
    if ($updated -cne '<YYYY-MM-DD>') {
        $null = Get-RecordDate $updated
        if ([string]::CompareOrdinal($updated, $created) -lt 0) { throw 'Updated date precedes Created date.' }
        if ([string]::CompareOrdinal($date, $updated) -lt 0) { throw 'Stamp date precedes current Updated date.' }
    }
    $content = [regex]::Replace($content, '(?m)^Created:[^\r\n]*', "Created: $created")
    $content = [regex]::Replace($content, '(?m)^Updated:[^\r\n]*', "Updated: $date")
    $temporary = $path + '.stamp.' + [Guid]::NewGuid().ToString('N')
    try {
        $stream = New-Object IO.FileStream($temporary, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
        try {
            $bytes = $encoding.GetBytes($content)
            $stream.Write($bytes, 0, $bytes.Length)
            $stream.Flush()
        } finally { $stream.Dispose() }
        [IO.File]::Replace($temporary, $path, [NullString]::Value)
    } finally {
        if ([IO.File]::Exists($temporary)) { [IO.File]::Delete($temporary) }
    }
}

try {
    if ($arguments.Count -eq 0) { Show-Usage; exit 1 }
    $commandName = [string]$arguments[0]
    $script:operands = @($arguments | Select-Object -Skip 1)
    switch -CaseSensitive ($commandName) {
        { $_ -ceq '-h' -or $_ -ceq '--help' -or $_ -ceq 'help' } { Show-Usage; break }
        'slug' {
            Require-Count 1 1 'slug requires one quoted title.'
            # Lowercase ASCII only, before replacing all non-ASCII runs with separators.
            $lowerAscii = [Text.RegularExpressions.MatchEvaluator]{ param($match) $match.Value.ToLowerInvariant() }
            $slug = [regex]::Replace($script:operands[0], '[A-Z]', $lowerAscii)
            $slug = ($slug -creplace '[^a-z0-9]+', '-').Trim('-')
            if ($slug.Length -eq 0) { throw 'Title must contain an ASCII letter or digit.' }
            Write-Output $slug
            break
        }
        'history-path' {
            Require-Count 0 1 'history-path accepts at most one date.'
            Write-Output (Get-HistoryPath (Get-DateArgument 0))
            break
        }
        'init-history' {
            Require-Count 1 2 'init-history requires a project root and optional date.'
            $relative = Get-HistoryPath (Get-DateArgument 1)
            $root = Get-ProjectRoot $script:operands[0]
            $period = [IO.Path]::GetFileNameWithoutExtension($relative)
            Initialize-File (Join-Path $root $relative) ((Read-Template 'history').Replace('{{period}}', $period))
            break
        }
        'init-notes' {
            Require-Count 2 2 'init-notes requires a project root and existing item slug.'
            Assert-Slug $script:operands[1]
            $root = Get-ProjectRoot $script:operands[0]
            Initialize-File (Join-Path $root "docs/lusona/notes/$($script:operands[1]).md") ((Read-Template 'notes').Replace('{{slug}}', $script:operands[1]))
            break
        }
        { $_ -ceq 'init-change' -or $_ -ceq 'init-adr' } {
            $script:recordJson = $true
            Require-Count 2 3 "$commandName requires a project root, functional slug, and optional date."
            Create-Record $commandName.Substring(5) $script:operands[0] $script:operands[1] (Get-DateArgument 2)
            break
        }
        { $_ -ceq 'next-change' -or $_ -ceq 'next-adr' } {
            Require-Count 1 1 "$commandName requires one project root."
            Get-NextSequence $commandName.Substring(5) $script:operands[0]
            break
        }
        'stamp-header' {
            Require-Count 1 2 'stamp-header requires a file and optional date.'
            Stamp-Header $script:operands[0] (Get-DateArgument 1)
            break
        }
        default { Show-Usage; throw "Unknown command: $commandName" }
    }
    exit 0
} catch {
    if ($script:recordJson) { Write-RecordResponse 'error' $script:recordPath $_.Exception.Message }
    else { [Console]::Error.WriteLine(('work-record: ' + $_.Exception.Message)) }
    exit 1
}
