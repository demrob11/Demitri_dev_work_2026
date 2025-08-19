# PowerShell Git Alias Setup & Troubleshooting

## Overview

This guide explains how to set up convenient Git command aliases in PowerShell and resolve common issues when doing so.

---

## ✅ Recommended: Use Functions (Not Aliases) for Git Commands with Arguments

Aliases in PowerShell are limited and cannot handle strings or arguments like `"git commit -m"`. Instead, define functions:

```powershell
function gs { git status }
function gc { git commit -m $args }
function ga { git add $args }
function gp { git push }
function gl { git log --oneline --graph --decorate }
```

Usage:
```powershell
gc "Initial commit"
ga .
```

---

## ❌ Common Issues & Fixes

### Issue 1: Alias not recognized
```powershell
gs
# Error: The term 'git status' is not recognized...
```
**Fix:** Ensure Git is installed and available in your system's `$PATH`. Use a function instead of alias for `gs`.

---

### Issue 2: Alias is read-only
```powershell
Set-Alias gc "git commit -m"
# Error: Alias is not writeable because alias 'gc' is read-only...
```
**Cause:** `gc` is a protected alias for `Get-Content` in PowerShell.

**Fix (Not Recommended):**
```powershell
Remove-Item alias:gc
Set-Alias gc git
```
**Better Fix:** Use a function instead, as shown above.

---

## 🔁 Auto-load Aliases on Startup

To persist your custom aliases/functions:

### 1. Open PowerShell Profile
```powershell
notepad $PROFILE
```

### 2. Add Functions
```powershell
function gs { git status }
function gc { git commit -m $args }
function ga { git add $args }
function gp { git push }
function gl { git log --oneline --graph --decorate }
```

### 3. Reload Profile
```powershell
. $PROFILE
```

---

## 🧠 Tip: Streamline Git Workflows in PowerShell
- Use `g` as your base alias prefix
- Create expressive, short commands for daily use
- Encapsulate logic in functions to boost clarity and reuse

---

*Crafted for developers optimizing their PowerShell + Git experience.*

