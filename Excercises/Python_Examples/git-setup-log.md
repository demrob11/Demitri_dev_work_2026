🪟 Windows Shortcuts Used During Setup
Action	Shortcut
Open Search / Run Command	Windows + S
Open Terminal or App in Split View	Windows + → or ←
Create New Desktop	Windows + Ctrl + D
Toggle Between Desktops	Windows + Ctrl + ←/→
Snap Window to Corner	Windows + ↑/↓ after side
File Explorer Shortcut	Windows + E
Task View (desktop overview)	Windows + Tab
🔧 Reusable PowerShell Git Setup Script
📄 setup-repo.ps1

This script automates the full Git initialization process and push to GitHub.

# setup-repo.ps1
# Initial Git repo setup for Python Study Log

cd "C:\Users\demit\OneDrive\Desktop\SoftwareDevDocuments2026"

# Initialize Git
git init

# Create .gitignore file
'__pycache__/' + "`n" + '*.pyc' + "`n" + '.env' + "`n" + '*.egg-info/' | Out-File -Encoding utf8 .gitignore

# Stage and commit all files
git add .
git commit -m "Initial commit - setup via PowerShell script"

# Link to GitHub (update with your actual URL if needed)
git remote add origin https://github.com/demrob11/Python-Study_log.git
git branch -M main
git push -u origin main

📥 How to Add This Script to Your Git Repo

Open PowerShell in your project folder.

Create the file:

notepad setup-repo.ps1


Paste the script above and save it.

Add and commit it to your repo:

git add setup-repo.ps1
git commit -m "Add PowerShell Git setup script"
git push

📁 Suggested Folder Structure
Python-Study_log/
├── lessons/
│   ├── 01-variables.py
│   ├── ...
├── scripts/
│   ├── setup-repo.ps1
│
├── README.md
├── git-setup-log.md
└── .gitignore

🎯 Purpose of This Document

Reference for setting up new Git projects with PowerShell

Reusable script and workflow guide for future automation

Teaching tool for Windows-based Git workflows

Tracks personal progress and professional polish

🚀 Next Steps

Create scripts/ and lessons/ folders

Add first Python lesson (01-variables.py)

Commit and push changes regularly

Build toward automation and branching structure


---

Would you like to save this file now in PowerShell?  
If yes, just run:

```powershell
notepad git-setup-log.md


Paste this content, save, then run:

git add git-setup-log.md
git commit -m "Add full Git setup documentation"
git push