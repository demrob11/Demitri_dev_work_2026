Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\demit> cd C:\Users\demit\GitHub\Demitri_dev_work_2026
PS C:\Users\demit\GitHub\Demitri_dev_work_2026> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        notes/Lithography/Lithography_and_FBX.md

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\demit\GitHub\Demitri_dev_work_2026> git remote -v
origin  https://github.com/demrob11/Demitri_dev_work_2026.git (fetch)
origin  https://github.com/demrob11/Demitri_dev_work_2026.git (push)
PS C:\Users\demit\GitHub\Demitri_dev_work_2026> git add .
PS C:\Users\demit\GitHub\Demitri_dev_work_2026> git commit -m "Added notes on FBX (as a fun concept)"
[main e2bdc67] Added notes on FBX (as a fun concept)
 1 file changed, 74 insertions(+)
 create mode 100644 notes/Lithography/Lithography_and_FBX.md
PS C:\Users\demit\GitHub\Demitri_dev_work_2026> git push
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 1.81 KiB | 1.81 MiB/s, done.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/demrob11/Demitri_dev_work_2026.git
   dd58c49..e2bdc67  main -> main
PS C:\Users\demit\GitHub\Demitri_d