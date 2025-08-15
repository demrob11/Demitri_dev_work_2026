# 🗃️ How to Remove Files from GitHub But Keep Them Locally

---

## 🧠 Purpose

Sometimes you add a file to your GitHub repo by accident — like a `.pdf`, `.zip`, or private document — but still want to keep it on your computer.

This guide explains how to:

* ✅ Remove files from **GitHub**
* ✅ Keep them **on your local machine**
* ✅ Prevent Git from **tracking them again**
* ✅ Maintain a clean and professional public repository

---

## ✅ Step-by-Step Instructions

### 🔹 1. Navigate to Your Git Repo Folder in PowerShell

```powershell
cd "C:\Users\demit\OneDrive\Desktop\SoftwareDevDocuments2026"
```

### 🔹 2. Untrack Files Using `git rm --cached`

```powershell
git rm --cached "Demitri_Career_Cert_Plan_2026.pdf"
git rm --cached "Exercises.zip"
git rm --cached "YOURPYTHON.pdf"
```

### 🔹 3. Commit the Removal

```powershell
git commit -m "Remove local-only files from GitHub but keep them on disk"
```

### 🔹 4. Push the Changes

```powershell
git push
```

### 🔹 5. Update `.gitignore` to Prevent Re-adding

Add to `.gitignore`:

```plaintext
*.pdf
*.zip
YOURPYTHON.pdf
Demitri_Career_Cert_Plan_2026.pdf
Exercises.zip
```

Commit and push:

```powershell
git add .gitignore
git commit -m "Update .gitignore to prevent re-adding removed files"
git push
```

---

## 📌 How to Commit *This* Markdown File to Your Repo

1. Make sure you’re in your repo folder:

```powershell
cd "C:\Users\demit\OneDrive\Desktop\SoftwareDevDocuments2026"
```

2. Save this file locally as `remove-files-but-keep-local.md`.
3. Stage it:

```powershell
git add remove-files-but-keep-local.md
```

4. Commit it:

```powershell
git commit -m "Add guide on removing files from GitHub but keeping them locally"
```

5. Push it:

```powershell
git push
```

---

## 📚 Related Resources

* [GitHub Docs: Ignoring Files](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files)
* [YouTube: PowerShell for Beginners](https://www.youtube.com/watch?v=Hmkyn4yoLNQ)
* [YouTube: Learn Git in 15 Minutes](https://www.youtube.com/watch?v=USjZcfj8yxE)
