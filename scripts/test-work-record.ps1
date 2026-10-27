# Behavioral checks; generated projects stay in repository-local tmp/.
$ErrorActionPreference = 'Stop'
$repository = Split-Path -Parent $PSScriptRoot
$helper = Join-Path $repository 'plugins/lusona/scripts/work-record.ps1'
$hostExecutable = (Get-Process -Id $PID).Path
$scratch = Join-Path $repository ('tmp/work-record-powershell-test.' + [Guid]::NewGuid().ToString('N'))
[IO.Directory]::CreateDirectory($scratch) | Out-Null
$utf8 = New-Object Text.UTF8Encoding($false)
[Console]::OutputEncoding = $utf8
$script:checks = 0

function Equal($actual, $expected) {
    $script:checks++
    if ($actual -cne $expected) { throw "Expected <$expected>, got <$actual>" }
}
function Write-Text($path, $value) { [IO.File]::WriteAllText($path, $value, $utf8) }
function Get-EncodedInvocation([string[]]$arguments, [string]$entry = $helper, [string]$setup = '') {
    # EncodedCommand preserves empty, quoted and multiline arguments on Windows PowerShell 5.1.
    $literals = @($arguments | ForEach-Object { "'" + $_.Replace("'", "''") + "'" })
    $source = $setup + "`n" + '$invocationArguments = @(' + ($literals -join ',') + "); & '" + $entry.Replace("'", "''") + "' @invocationArguments; exit " + '$LASTEXITCODE'
    return [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($source))
}
function Invoke-Helper([string[]]$arguments, [int]$code = 0, [string]$entry = $helper, [string]$setup = '') {
    $encoded = Get-EncodedInvocation $arguments $entry $setup
    $priorPreference = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $output = & $hostExecutable -NoProfile -NonInteractive -EncodedCommand $encoded 2> (Join-Path $scratch 'stderr.txt')
    $actualCode = $LASTEXITCODE
    $ErrorActionPreference = $priorPreference
    if ($actualCode -ne $code) {
        throw "Command [$($arguments -join ', ')] expected exit $code, got $actualCode. Output: $output. Error: $([IO.File]::ReadAllText((Join-Path $scratch 'stderr.txt')))"
    }
    Equal $actualCode $code
    return ($output -join "`n")
}
function Reject([string[]]$arguments) { Invoke-Helper $arguments 1 | Out-Null }
function Start-Helper([string[]]$arguments) {
    $configuration = New-Object Diagnostics.ProcessStartInfo
    $configuration.FileName = $hostExecutable
    $configuration.Arguments = '-NoProfile -NonInteractive -EncodedCommand ' + (Get-EncodedInvocation $arguments)
    $configuration.UseShellExecute = $false
    $configuration.CreateNoWindow = $true
    $configuration.RedirectStandardOutput = $true
    $configuration.RedirectStandardError = $true
    $configuration.StandardOutputEncoding = $utf8
    $process = New-Object Diagnostics.Process
    $process.StartInfo = $configuration
    $null = $process.Start()
    return $process
}

try {
    Equal (Invoke-Helper @('slug', '  JS/TS path aliases!  ')) 'js-ts-path-aliases'
    Equal (Invoke-Helper @('slug', "Rust`n`nbackend")) 'rust-backend'
    Equal (Invoke-Helper @('slug', ([char]0x130 + ' ABC ' + [char]0x00e9))) 'abc'
    Reject @('slug', '!!!')
    Reject @('unknown')
    Reject @('slug')
    foreach ($pair in @('01:01', '07:01', '08:02', '14:02', '15:03', '21:03', '22:04', '28:04', '29:05', '30:05')) {
        $parts = $pair.Split(':')
        Equal (Invoke-Helper @('history-path', "2026-09-$($parts[0])")) "docs/lusona/history/2026-09-week-$($parts[1]).md"
    }
    Equal (Invoke-Helper @('history-path', '0001-01-01')) 'docs/lusona/history/0001-01-week-01.md'
    Equal (Invoke-Helper @('history-path', '2000-02-29')) 'docs/lusona/history/2000-02-week-05.md'
    foreach ($date in @('', '0000-01-01', '1900-02-29', '2026-02-29', '2026-04-31', '2026-13-01', '26-01-01')) { Reject @('history-path', $date) }
    $project = Join-Path $scratch 'project with spaces'
    [IO.Directory]::CreateDirectory($project) | Out-Null
    $history = Invoke-Helper @('init-history', $project, '2026-09-10')
    Equal $history (Join-Path $project 'docs/lusona/history/2026-09-week-02.md')
    $notes = Invoke-Helper @('init-notes', $project, 'rust-backend')
    foreach ($item in @(@('init-history', '2026-09-14', $history), @('init-notes', 'rust-backend', $notes))) {
        $before = [IO.File]::ReadAllText($item[2]) + "`nKeep this evidence.`n"
        Write-Text $item[2] $before
        Equal (Invoke-Helper @($item[0], $project, $item[1])) $item[2]
        Equal ([IO.File]::ReadAllText($item[2])) $before
    }
    foreach ($slug in @('../escape', 'MixedCase', 'a--b', ('caf' + [char]0xe9))) { Reject @('init-notes', $project, $slug) }
    Reject @('init-history', (Join-Path $scratch 'missing'), '2026-09-10')
    $bundle = Join-Path $scratch 'relocated plugin'
    [IO.Directory]::CreateDirectory((Join-Path $bundle 'scripts')) | Out-Null
    [IO.Directory]::CreateDirectory((Join-Path $bundle 'templates')) | Out-Null
    Copy-Item -LiteralPath $helper -Destination (Join-Path $bundle 'scripts/work-record.ps1')
    foreach ($name in @('history', 'notes', 'spec', 'adr')) {
        $original = [IO.File]::ReadAllText((Join-Path $repository "plugins/lusona/templates/$name.md"))
        Write-Text (Join-Path $bundle "templates/$name.md") ($original + "`nBundle-specific $name content.`n")
    }
    $relocated = Join-Path $bundle 'scripts/work-record.ps1'
    $relocatedHistory = Invoke-Helper @('init-history', $project, '2026-09-15') 0 $relocated
    Equal ([IO.File]::ReadAllText($relocatedHistory).Contains('Bundle-specific history content.')) $true
    $relocatedNotes = Invoke-Helper @('init-notes', $project, 'probe') 0 $relocated
    Equal ([IO.File]::ReadAllText($relocatedNotes).Contains('Bundle-specific notes content.')) $true
    foreach ($kind in @('change', 'adr')) {
        $response = (Invoke-Helper @("init-$kind", $project, 'add-python-support', '2026-09-26')) | ConvertFrom-Json
        $directory = if ($kind -eq 'change') { 'specs' } else { 'adr' }
        Equal $response.status 'created'
        Equal $response.path (Join-Path $project "docs/lusona/$directory/20260926-add-python-support.md")
        $before = [IO.File]::ReadAllText($response.path)
        Equal $before.Contains('Created: 2026-09-26') $true
        Equal $before.Contains('Updated: 2026-09-26') $true
        $conflict = (Invoke-Helper @("init-$kind", $project, 'add-python-support', '2026-09-26') 3) | ConvertFrom-Json
        Equal $conflict.status 'conflict'
        Equal $conflict.path $response.path
        Equal ([IO.File]::ReadAllText($response.path)) $before
        foreach ($slug in @('../escape', 'MixedCase', 'a--b')) {
            Equal ((Invoke-Helper @("init-$kind", $project, $slug, '2026-09-26') 1 | ConvertFrom-Json).status) 'error'
        }
        Equal ((Invoke-Helper @("init-$kind", $project, 'invalid-date', '2026-02-29') 1 | ConvertFrom-Json).status) 'error'
        Equal ((Invoke-Helper @("init-$kind") 1 | ConvertFrom-Json).status) 'error'
        $directoryConflict = Join-Path $project "docs/lusona/$directory/20260926-directory.md"
        [IO.Directory]::CreateDirectory($directoryConflict) | Out-Null
        Equal ((Invoke-Helper @("init-$kind", $project, 'directory', '2026-09-26') 3 | ConvertFrom-Json).status) 'conflict'
        $relocatedRecord = Invoke-Helper @("init-$kind", $project, 'relocated', '0001-01-01') 0 $relocated | ConvertFrom-Json
        $templateName = if ($kind -eq 'change') { 'spec' } else { 'adr' }
        Equal ([IO.File]::ReadAllText($relocatedRecord.path).Contains("Bundle-specific $templateName content.")) $true
        $today = [datetime]::Now.ToString('yyyyMMdd', [Globalization.CultureInfo]::InvariantCulture)
        $defaultRecord = Invoke-Helper @("init-$kind", $project, 'default-date') | ConvertFrom-Json
        Equal $defaultRecord.path (Join-Path $project "docs/lusona/$directory/$today-default-date.md")
        $raceArguments = @("init-$kind", $project, 'same-function', '2026-09-26')
        $first = Start-Helper $raceArguments
        $second = Start-Helper $raceArguments
        try {
            $firstOutput = $first.StandardOutput.ReadToEnd()
            $secondOutput = $second.StandardOutput.ReadToEnd()
            $first.WaitForExit()
            $second.WaitForExit()
            Equal ((@($first.ExitCode, $second.ExitCode) | Sort-Object) -join ',') '0,3'
            Equal ((@(($firstOutput | ConvertFrom-Json).status, ($secondOutput | ConvertFrom-Json).status) | Sort-Object) -join ',') 'conflict,created'
            $racePath = Join-Path $project "docs/lusona/$directory/20260926-same-function.md"
            Equal ([IO.File]::ReadAllText($racePath)) ($before.Replace('20260926-add-python-support', '20260926-same-function'))
        } finally { $first.Dispose(); $second.Dispose() }
    }
    # Quotes, backslashes and newlines are legal path characters on Unix; Windows excludes them.
    $unicodeName = 'unicode-' + [char]0x65e5 + [char]0x672c + [char]::ConvertFromUtf32(0x1f680)
    $unusualName = if ([IO.Path]::DirectorySeparatorChar -eq '/') { "quoted`"-backslash\-newline`nproject-$unicodeName" } else { "apostrophe'-$unicodeName" }
    $unusual = Join-Path $scratch $unusualName
    [IO.Directory]::CreateDirectory($unusual) | Out-Null
    $unusualResponse = Invoke-Helper @('init-change', $unusual, 'json-path', '2026-09-26') | ConvertFrom-Json
    Equal $unusualResponse.path (Join-Path $unusual 'docs/lusona/specs/20260926-json-path.md')
    Equal ((Invoke-Helper @('init-change', (Join-Path $scratch 'missing'), 'valid-slug') 1 | ConvertFrom-Json).status) 'error'
    $blocked = Join-Path $scratch 'blocked'
    [IO.Directory]::CreateDirectory($blocked) | Out-Null
    Write-Text (Join-Path $blocked 'docs') 'preserve'
    Equal ((Invoke-Helper @('init-change', $blocked, 'write-failure') 1 | ConvertFrom-Json).status) 'error'
    Equal ([IO.File]::ReadAllText((Join-Path $blocked 'docs'))) 'preserve'
    # Inject an exclusive-open race with Windows' exception type, through the real CLI.
    $directoryRace = @'
function New-Object {
    param([string]$TypeName, [object[]]$ArgumentList)
    if ($TypeName -eq 'IO.FileStream') {
        [IO.Directory]::CreateDirectory($ArgumentList[0]) | Out-Null
        throw (New-Object UnauthorizedAccessException 'Simulated directory race at exclusive open.')
    }
    Microsoft.PowerShell.Utility\New-Object -TypeName $TypeName -ArgumentList $ArgumentList
}
'@
    $raceResponse = Invoke-Helper @('init-change', $project, 'directory-race', '2026-09-26') 3 $helper $directoryRace | ConvertFrom-Json
    Equal $raceResponse.status 'conflict'
    Equal ([IO.Directory]::Exists($raceResponse.path)) $true
    # A failure after ownership is acquired must stay error1 and remove partial output.
    $writeFailure = @'
function New-Object {
    param([string]$TypeName, [object[]]$ArgumentList)
    if ($TypeName -eq 'IO.FileStream') {
        [IO.File]::WriteAllText($ArgumentList[0], 'partial')
        $stream = [pscustomobject]@{}
        $stream | Add-Member ScriptMethod Write { throw (New-Object IO.IOException 'Simulated write failure.') }
        $stream | Add-Member ScriptMethod Flush { }
        $stream | Add-Member ScriptMethod Dispose { }
        return $stream
    }
    Microsoft.PowerShell.Utility\New-Object -TypeName $TypeName -ArgumentList $ArgumentList
}
'@
    $failedWrite = Invoke-Helper @('init-change', $project, 'failed-write', '2026-09-26') 1 $helper $writeFailure | ConvertFrom-Json
    Equal $failedWrite.status 'error'
    Equal (Test-Path -LiteralPath $failedWrite.path) $false
    $numbered = Join-Path $scratch 'numbered'
    [IO.Directory]::CreateDirectory($numbered) | Out-Null
    Equal (Invoke-Helper @('next-change', $numbered)) '0001'
    Equal (Invoke-Helper @('next-adr', $numbered)) '0001'
    $locationSetup = "Set-Location -LiteralPath '" + $scratch.Replace("'", "''") + "'"
    Equal (Invoke-Helper @('next-change', 'numbered') 0 $helper $locationSetup) '0001'
    Equal (Test-Path -LiteralPath (Join-Path $numbered 'docs')) $false
    foreach ($dir in @('specs', 'plans', 'adr')) { [IO.Directory]::CreateDirectory((Join-Path $numbered "docs/lusona/$dir")) | Out-Null }
    foreach ($name in @('specs/0042-shared.md', 'plans/0042-shared.md', 'plans/0048-standalone.md', 'specs/legacy.md', 'adr/README.md', 'adr/0009-later.md', 'specs/20260926-dated.md')) { Write-Text (Join-Path $numbered "docs/lusona/$name") '' }
    Equal (Invoke-Helper @('next-change', $numbered)) '0049'
    Equal (Invoke-Helper @('next-adr', $numbered)) '0010'
    foreach ($name in @('specs/0048-conflict.md', 'specs/49-malformed.md', 'specs/0000-zero.md', 'specs/2026-09-26-date.md', 'specs/20260229-invalid-date.md', 'specs/0049-Mixed.md', 'adr/README-copy.md', 'adr/0009-conflict.md', 'adr/9999-last.md')) {
        $path = Join-Path $numbered "docs/lusona/$name"
        Write-Text $path ''
        $command = if ($name.StartsWith('adr/')) { 'next-adr' } else { 'next-change' }
        Reject @($command, $numbered)
        [IO.File]::Delete($path)
    }
    # Header replacement preserves exact bytes outside the two fields, including CRLF and final newline choice.
    foreach ($newline in @("`n", "`r`n")) {
        foreach ($ending in @('', $newline)) {
            $path = Join-Path $scratch 'header.md'
            $before = (@('# Example', 'Created: <YYYY-MM-DD>', 'Updated: <YYYY-MM-DD>', '', 'Literal $HOME and `code`.') -join $newline) + $ending
            Write-Text $path $before
            Invoke-Helper @('stamp-header', $path, '2026-09-10') | Out-Null
            $expected = $before.Replace('<YYYY-MM-DD>', '2026-09-10')
            Equal ([IO.File]::ReadAllText($path)) $expected
            Invoke-Helper @('stamp-header', $path, '2026-09-12') | Out-Null
            $expected = $expected.Replace('Updated: 2026-09-10', 'Updated: 2026-09-12')
            Equal ([IO.File]::ReadAllText($path)) $expected
            Reject @('stamp-header', $path, '2026-09-11')
            Equal ([IO.File]::ReadAllText($path)) $expected
        }
    }
    foreach ($content in @("Created: 2026-09-10`nUpdated: 2026-09-09`n", "Created: <YYYY-MM-DD>`nUpdated: <YYYY-MM-DD>`nUpdated: <YYYY-MM-DD>`n", "Created:2026-09-10`nUpdated: 2026-09-10`n", "Created: 2026-02-29`nUpdated: 2026-09-10`n")) {
        $path = Join-Path $scratch 'invalid-header.md'
        Write-Text $path $content
        Reject @('stamp-header', $path, '2026-09-12')
        Equal ([IO.File]::ReadAllText($path)) $content
    }
    Reject @('stamp-header', (Join-Path $scratch 'missing.md'), '2026-09-12')
    # Symlinks can require privileges on Windows; exercise them whenever creation is available.
    $target = Join-Path $scratch 'target.md'
    Write-Text $target "Created: 2026-09-10`nUpdated: 2026-09-10`n"
    $link = Join-Path $scratch 'linked.md'
    try { New-Item -ItemType SymbolicLink -Path $link -Target $target -ErrorAction Stop | Out-Null } catch { Write-Warning 'Symlink checks skipped: symlink creation unavailable.' }
    if (Test-Path -LiteralPath $link) {
        Reject @('stamp-header', $link, '2026-09-12')
        $recordLink = Join-Path $project 'docs/lusona/specs/20260926-linked.md'
        New-Item -ItemType SymbolicLink -Path $recordLink -Target $target | Out-Null
        Equal ((Invoke-Helper @('init-change', $project, 'linked', '2026-09-26') 3 | ConvertFrom-Json).status) 'conflict'
        $notesLink = Join-Path $project 'docs/lusona/notes/linked.md'
        New-Item -ItemType SymbolicLink -Path $notesLink -Target $target | Out-Null
        Reject @('init-notes', $project, 'linked')
        $legacyLink = Join-Path $numbered 'docs/lusona/adr/0010-linked.md'
        New-Item -ItemType SymbolicLink -Path $legacyLink -Target $target | Out-Null
        Reject @('next-adr', $numbered)
        [IO.File]::Delete($target)
        Equal ((Invoke-Helper @('init-change', $project, 'linked', '2026-09-26') 3 | ConvertFrom-Json).status) 'conflict'
    }
    Write-Output "PowerShell work-record behavioral checks passed ($script:checks assertions)."
} finally {
    Remove-Item -LiteralPath $scratch -Recurse -Force
}
