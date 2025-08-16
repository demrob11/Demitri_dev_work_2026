git add <filename>        # Add a single file
git add .                 # Add all changes in the current directory
git add -A                # Add all changes in the repo (new, modified, deleted)

**********************************

git rm --cached <filename>   # Untrack file but keep it on disk
**********************************

git rm <filename>
**********************************

git commit -m "Your commit message here"
**********************************

git push  (pushes changes)
**********************************

git add -A        #add all changes
**********************************

__________________________________________________________________________________

# Make the folder
mkdir MyEmptyFolder

# Add a placeholder file
New-Item -Path "MyEmptyFolder\.gitkeep" -ItemType File

# Stage and commit
git add MyEmptyFolder/.gitkeep
git commit -m "Add empty folder MyEmptyFolder"
************************************************************************

# Remove an empty folder from the repo (keep locally)
git rm --cached MyEmptyFolder/.gitkeep
git commit -m "Remove MyEmptyFolder from repo"
************************************************************************

# Remove the folder entirely (repo + local machine)
Remove-Item -Recurse -Force MyEmptyFolder
git rm -r MyEmptyFolder
git commit -m "Delete MyEmptyFolder"
***********************************************************************

# Git Remove all empty folders (keep locally)

git ls-files "*.gitkeep" | ForEach-Object { git rm --cached $_ }

git commit -m "Remove empty folders from repo"
git push

# Move a file to another directory

Move-Item "C:\Path\To\File.txt" "C:\New\Directory\"
**********************************************************************

# Overwrite without prompting (pS7+)

Move-Item "C:\Path\To\File.txt" "C:\New\Directory\" -Force
**********************************************************************

# Move several specific files:

Move-Item "C:\Path\To\File1.txt","C:\Path\To\File2.txt","C:\Path\To\File3.txt" "C:\New\Directory\"
**********************************************************************

# Move all files of a certain type from one folder:

Move-Item "C:\Path\To\*.txt" "C:\New\Directory\"
**********************************************************************

# Move multiple different extensions

Move-Item "C:\Path\To\*.txt","C:\Path\To\*.docx" "C:\New\Directory\"
***********************************************************************




