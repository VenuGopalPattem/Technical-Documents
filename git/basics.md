# Git Basics

This document explains Git from a foundational perspective, including its importance, installation, workflow, and commands. It also provides a blueprint of the areas in Git and which commands work where.

---

## What is Git?

Git is a **version control system** that tracks changes in files and code over time. It allows multiple developers to work on the same project, revert to previous versions, and track the history of changes.

---

## Importance of Git

- Tracks changes to files and code  
- Allows collaboration  
- Provides a safe way to experiment and revert changes  


---

## What is GitHub?

GitHub is an **online hosting service for Git repositories**. It allows you to:

- Store code remotely   
- Backup and share projects  

> Git is the tool, GitHub is the platform to host Git repositories online.

---

## Installation in Linux

To check if Git is installed:

```bash
git --version
```

If Git is not installed, use:

```bash
sudo apt update
sudo apt install git
```

After installation, configure your Git account:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---

## Git Workflow Blueprint

When working with Git, your code moves through **different stages or areas** before reaching the remote repository. The flow looks like this:

```
Working Directory --> Staging Area --> Local Repository --> Remote Repository
```

---

### Stage Descriptions

| Stage / Area | What Happens | Relevant Commands |
|--------------|--------------|-----------------|
| **Working Directory** | Your actual files on disk. You edit and modify files here. | `edit file.txt`, `rm file.txt` |
| **Staging Area (Index)** | Files added here are **ready to commit**. Only staged files will be saved in the next commit. | `git add file.txt`, `git reset file.txt` |
| **Local Repository** | Snapshots of staged files are saved here as commits. Git tracks all changes in `.git/` | `git commit -m "message"`, `git revert <commit>`, `git reset <commit>` |
| **Remote Repository** | Your commits are uploaded here (e.g., GitHub). Other developers can access these changes. | `git push`, `git fetch`, `git pull` |

---

### Commands by Stage (Reference Table)

| Area | What You Can Do | Commands / Examples |
|------|----------------|------------------|
| Working Directory | Edit, delete, move files | `vim file.txt`, `rm file.txt`, `mv file.txt folder/` |
| Staging Area | Add changes, unstage files | `git add file.txt`, `git add .`, `git reset file.txt` |
| Local Repository | Save snapshots, undo commits | `git commit -m "message"`, `git revert <commit-hash>`, `git reset <commit-hash>` |
| Remote Repository | Push or sync changes | `git push origin main`, `git pull origin main`, `git fetch origin` |

---

### Important Notes on Commands

- `git reset file.txt` **only works in the staging area**. If you run it **after pushing to remote**, it does **not affect remote history**.  
- `git revert <commit>` is the safe way to undo commits that have already been pushed.  
- `git checkout -- file.txt` discards changes in the working directory.  
- `git diff` shows differences between working directory and staging area or between commits.  
- Branching and merging allow parallel development (advanced concept, can be added later).

---

### Example Workflow

1. **Initialize repository**
```bash
git init
```

2. **Check status**
```bash
git status
```

3. **Stage files**
```bash
git add file1.txt file2.txt
```

4. **Commit changes**
```bash
git commit -m "Added initial files"
```

5. **Link to remote**
```bash
git remote add origin <repo-url>
```

6. **Push changes**
```bash
git push -u origin main
```

7. **Undo changes if needed**
```bash
git reset file2.txt        # unstage
 git checkout -- file2.txt  # discard changes in working directory
 git revert <commit-hash>   # undo pushed commit safely
```

## Git Commands Reference by Area

| Area | Command | Purpose / Usage | Notes / Important Info |
|------|---------|----------------|-----------------------|
| **Working Directory** | `vim file.txt` / `nano file.txt` | Edit files | Any changes you make are local until staged |
| | `rm file.txt` | Delete a file | Deletes from working directory |
| | `mv file.txt folder/` | Move or rename a file | Changes will be detected by Git |
| | `git checkout -- file.txt` | Discard changes in working directory | Resets file to last committed state |
| | `git diff` | Show differences between working directory and staging | Helps see what changed before adding |
| **Staging Area (Index)** | `git add file.txt` | Stage a file | Moves file to staging area ready to commit |
| | `git add .` | Stage all changes | Adds all modified/untracked files |
| | `git reset file.txt` | Unstage a file | Moves file back to working directory |
| | `git diff --staged` | Show differences between staged files and last commit | Useful before committing |
| **Local Repository** | `git commit -m "message"` | Save a snapshot of staged files | Commit creates history in local repo |
| | `git revert <commit-hash>` | Undo a commit safely | Creates a new commit that reverses changes |
| | `git reset <commit-hash>` | Move HEAD to a previous commit | Can modify history; use carefully |
| | `git log` | View commit history | Shows commit hash, author, date, message |
| | `git show <commit-hash>` | Show details of a specific commit | Shows changes made in that commit |
| **Remote Repository** | `git remote add origin <url>` | Link local repo to remote | Sets up connection to GitHub/other remote |
| | `git push origin main` | Upload commits to remote | `-u` sets upstream for future pushes |
| | `git pull origin main` | Fetch and merge remote changes | Keeps local repo updated |
| | `git fetch origin` | Download commits from remote without merging | Allows inspection before merge |
| | `git clone <url>` | Copy a remote repo locally | Creates new working directory and local repo |



---
