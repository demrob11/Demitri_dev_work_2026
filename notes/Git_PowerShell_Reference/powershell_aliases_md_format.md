# PowerShell Alias Reference (Python & Git Focus)

This Markdown-friendly version provides a categorized reference of PowerShell aliases, with emphasis on workflows relevant to **Python development**, **Git usage**, and **DevOps tooling**.

---

## How to Use This Document

Each section contains a table of aliases grouped by task. View directly or fold/unfold in Markdown viewers that support collapsible content.

---

## Understanding `gal` (Get-Alias)

The `gal` alias is short for:

```powershell
gal → Get-Alias
```

### Why It's Important

| Use Case            | Benefit                                                          |
| ------------------- | ---------------------------------------------------------------- |
| Discover aliases    | Quickly look up what command an alias points to                  |
| Translate scripts   | Map shorthand (like `ls`, `rm`) to full PowerShell cmdlets       |
| Find custom aliases | Check what user-defined shortcuts are active in your session     |
| Reverse lookup      | Use `gal -Definition CommandName` to find aliases for any cmdlet |

### Examples

#### Industry Production Scenarios

```powershell
# Check if a CI/CD script alias exists for triggering a pipeline
Set-Alias run-ci "& .\scripts\trigger-build.ps1"
gal run-ci

# Verify aliases for test automation or deployment wrappers
gal runtests
gal deploytest

# Audit all session aliases and export them for documentation or audits
Get-Alias | Where-Object { $_.Source -eq 'Alias' } | Export-Csv .\alias-audit.csv

# Check for deprecated or legacy aliases in enterprise scripts
gal oldtask
gal -Definition Out-Null

# Open PowerShell profile to inspect or define persistent aliases
notepad $PROFILE
```

#### General Alias Discovery

```powershell
# Look up what 'ls' really does
gal ls

# Show all aliases for Get-Content
gal -Definition Get-Content

# View all defined aliases, sorted alphabetically
gal | Sort-Object Name
```

**Tip:** Use `gal` regularly when learning PowerShell, troubleshooting scripts, inspecting custom environments, or reverse-engineering automation pipelines.

#### Git Context Example

```powershell
# Check if any PowerShell aliases are masking Git commands
gal git

# If you've aliased 'gs' or 'glog' in your PowerShell profile, verify them:
gal gs
gal glog

# Confirm 'git' is invoking the correct executable
Get-Command git
```

```powershell
# Define Git helpers for future reuse
Set-Alias gs "git status"
Set-Alias glog "git log --oneline --graph"
```

---

## File System & Navigation

| Alias   | Full Command      | Description                   |
| ------- | ----------------- | ----------------------------- |
| `ls`    | `Get-ChildItem`   | List items in a directory     |
| `dir`   | `Get-ChildItem`   | Same as `ls`                  |
| `gci`   | `Get-ChildItem`   | More verbose listing          |
| `cd`    | `Set-Location`    | Change directory              |
| `sl`    | `Set-Location`    | Shortcut to `cd`              |
| `pwd`   | `Get-Location`    | Show current directory        |
| `..`    | `Set-Location ..` | Go up one directory           |
| `pushd` | `Push-Location`   | Save current location         |
| `popd`  | `Pop-Location`    | Return to last saved location |

---

## File Operations

| Alias   | Full Command  | Description                 |
| ------- | ------------- | --------------------------- |
| `cp`    | `Copy-Item`   | Copy files                  |
| `copy`  | `Copy-Item`   | Same as `cp`                |
| `mv`    | `Move-Item`   | Move or rename files        |
| `move`  | `Move-Item`   | Same as `mv`                |
| `rm`    | `Remove-Item` | Delete file or folder       |
| `del`   | `Remove-Item` | Same as `rm`                |
| `erase` | `Remove-Item` | Same as `rm`                |
| `ni`    | `New-Item`    | Create new file/folder      |
| `md`    | `New-Item`    | Also used to create folders |
| `mkdir` | `New-Item`    | Directory creation          |
| `ri`    | `Remove-Item` | Remove file/folder          |
| `rmdir` | `Remove-Item` | Remove directories          |

---

## Content & Output

| Alias         | Full Command   | Description                  |
| ------------- | -------------- | ---------------------------- |
| `cat`         | `Get-Content`  | Show file contents           |
| `type`        | `Get-Content`  | Same as `cat`                |
| `gc`          | `Get-Content`  | More concise                 |
| `echo`        | `Write-Output` | Print to screen              |
| `write`       | `Write-Output` | Same as `echo`               |
| `tee`         | `Tee-Object`   | Output to console *and* file |
| `sc`          | `Set-Content`  | Overwrite file content       |
| `add-content` | `Add-Content`  | Append to file               |
| `out`         | `Out-Default`  | Pipe data to output          |
| `out-null`    | `Out-Null`     | Suppress output              |

---

## Search & Filter

| Alias     | Full Command     | Description                            |
| --------- | ---------------- | -------------------------------------- |
| `%`       | `ForEach-Object` | Loop or map-like ops                   |
| `foreach` | `ForEach-Object` | Same as `%`                            |
| `?`       | `Where-Object`   | Filter elements                        |
| `where`   | `Where-Object`   | Same as `?`                            |
| `sls`     | `Select-String`  | Grep-like search                       |
| `findstr` | `Select-String`  | Alias for compatibility with CMD users |

---

## System & Processes

| Alias   | Full Command       | Description                  |
| ------- | ------------------ | ---------------------------- |
| `ps`    | `Get-Process`      | List running processes       |
| `gps`   | `Get-Process`      | Same as `ps`                 |
| `kill`  | `Stop-Process`     | End a process                |
| `sp`    | `Set-ItemProperty` | Set registry or config value |
| `gp`    | `Get-ItemProperty` | Get registry or config value |
| `gsv`   | `Get-Service`      | List services                |
| `start` | `Start-Process`    | Open a file or run app       |
| `ii`    | `Invoke-Item`      | Open file in default program |

---

## Miscellaneous / Niche

| Alias      | Full Command             | Description               |
| ---------- | ------------------------ | ------------------------- |
| `clc`      | `Clear-Content`          | Clear a file’s content    |
| `measure`  | `Measure-Object`         | Count lines/words/etc     |
| `select`   | `Select-Object`          | Choose fields from output |
| `sort`     | `Sort-Object`            | Sort output               |
| `group`    | `Group-Object`           | Group by property         |
| `limit`    | `Select-Object -First`   | Limit rows from output    |
| `history`  | `Get-History`            | Command history           |
| `h`        | `Get-History`            | Same as above             |
| `r`        | `Invoke-History`         | Re-run previous command   |
| `read`     | `Read-Host`              | Prompt user for input     |
| `ipconfig` | `Get-NetIPConfiguration` | Modern networking cmd     |

---

## View All Current Aliases in PowerShell

```powershell
Get-Alias | Sort-Object Name
```

To export them:

```powershell
Get-Alias | Export-Csv aliases.csv -NoTypeInformation
```

