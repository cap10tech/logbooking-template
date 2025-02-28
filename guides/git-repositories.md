# Git Logbook: Tracking Your Git Workflow

## Introduction

Log your Git operations systematically for efficient version control and debugging.

---

## Installing Git

- **Installing Git on Windows**

```shell
# Download Git for Windows
Visit https://git-scm.com/download/win

# Run the installer and follow the prompts

# Verify installation
git --version
```

> Ensure Git is added to PATH during installation.

---

- **Installing Git on macOS**

```shell
# Check if Git is installed
git --version

# Install Git via Homebrew
brew install git
```

> Homebrew simplifies package management for macOS.

---

- **Installing Git on Linux (Ubuntu/Debian)**

```shell
# Update package lists
sudo apt-get update

# Install Git
sudo apt-get install git

# Verify installation
git --version
```

> Recommended to keep Git updated via system package manager.

---

## Initializing and Cloning a Repository

- **Initializing a New Repository**

```shell
# Navigate to your project directory
cd ~/projects/my-repo

# Initialize Git
git init
```

> `git init` sets up a new Git repository in the specified directory.

---

- **Cloning an Existing Repository**

```shell
# Clone a repository using HTTPS
git clone https://github.com/user/repo.git

# Clone a repository using SSH
git clone git@github.com:user/repo.git
```

> SSH provides a more secure authentication method.

---

## Staging, Committing, and Pushing Changes

- **Staging Files for Commit**

```shell
# Stage all modified and new files
git add .

# Stage a specific file
git add file.txt
```

> Use `git status` to check staged files before committing.

---

- **Committing Changes**

```shell
git commit -m "Added new feature X"
```

> Keep commit messages descriptive and concise.

---

- **Pushing Changes to Remote Repository**

```shell
git push origin main
```

> Ensure your branch is up to date before pushing.

---

## Pulling and Synchronizing Changes

- **Pulling the Latest Changes**

```shell
git pull origin main
```

> Fetches and merges remote changes into your local branch.

---

- **Fetching Changes Without Merging**

```shell
git fetch origin
```

> Allows review of remote changes before merging.

---

## Resolving Merge Conflicts

- **Handling Merge Conflicts**

```shell
git status
```

> Identify files with conflicts.

---

```shell
# Open conflicting file, resolve conflicts, and mark as resolved
git add resolved-file.txt

# Commit resolved changes
git commit -m "Resolved merge conflict"
```

> Manually edit files to remove conflict markers.

---

## Branching and Collaboration

- **Creating and Switching Branches**

```shell
git checkout -b feature-branch
```

> Creates and switches to a new branch.

---

- **Merging Branches**

```shell
git checkout main
git merge feature-branch
```

> Ensure main is up to date before merging.

---

## Managing Pull Requests

- **Pushing a Feature Branch to Remote**

```shell
git push origin feature-branch
```

> Create a pull request via GitHub to merge into the main branch.

---

## Quick Git Command Reference

| Command | Description |
|---------|-------------|
| `git init` | Initialize a new repository |
| `git clone <url>` | Clone an existing repository |
| `git status` | Check repository status |
| `git add .` | Stage all changes |
| `git commit -m ""` | Commit changes with a message |
| `git push origin main` | Push changes to the main branch |
| `git pull origin main` | Pull updates from the remote repository |

---


