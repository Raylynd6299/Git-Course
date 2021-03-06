# Git-Manual

git has three main trees:
+ Working directory
+ Staging area
+ Repository

Notes:
+ Default Branch -> Master
+ HEAD is how we name the commit we are in

# Create a Repositor #
```Bash
	git init
```

# Add files and directory to staging area #
```Bash
# One by one		
	git add <file>
	
# All
	git add .
	git add -A 
```
# Remove a file or directory to staging area #
```Bash
# Files or Directorys  #
	git restore --staged <name>
# Files only
	git rm --cached <file name>
# Directories
	git rm --cached -r <directory name>
```
# To restore a file that has be modified and it's not in the repository stage yet #
```Bash
# This file should not be in staging area
	git restore <file name>
```

# To check the differences between the committed file and modifying the file #
```Bash
	git diff <file name>
```

# Do Commits #
```Bash
# Only commit
	git commit
# With message
	git commit -m "Message"
# Add all files and do commit with message
	git commit -am "Message"
```

# Travel in Time(Commits) or Branchs  #
```Bash
# Travel through commits
	git switch -d <commit ID>
	git checkout <commit ID>
# Switch Branch
	git switch <branch name>
# Create a Branch
	git switch -c <branch>
# Merge in a new Branch
	git switch -m <Branch>
# Return to master branch and (HEAD) commit
	git switch -
	git switch master
	git checkout master
```
# Reset #

We have *three* types of resets

+ *Reset soft*: This type of reset takes you to the selected commit, eliminating subsequent commits, but without modifying the Code or the workspace in any way.
### Syntax
```Bash
	git reset --soft <commit ID>
```
+ *Reser mixed*: This type of reset takes you to the selected commit, eliminating the subsequent commits and the files in the staging area but without modifying the Code or the workspace in any way.

+ *Reset hard*: This type of reset deletes everything that happened after the selected commit to go and turns it into the new master
### Syntax
```Bash
# Note: First do a travel in time (switch)
	git reset --hard <commit ID>
```

# Branches #

They are like a parallel realities

+ ### To see the Branches
```Bash
	git branch
```
+ ### To create a new branch
	The *new branch* will have all the information of the branch from where it was created
```Bash
	git branch <branch name>
```
+ ### To delete a branch
```Bash
	git branch -d <branch name>
```
+ ### To change Branches
	As shown above to switch to a different branch:
```Bash
	git switch <branch name>
	git checkout <branch name>
```
+ ### To Merge two Branches
	That doesn't delete the branch to merged
```Bash
# Note: the branch name refers to the branch that merges with the branch in which you are
	git merge <Branch name>
```
# GitHub #
##  Upload repository to Github ##

### To set your user of GitHub in your local repository
```Bash
	git config credential.username "usernameInGitGub"
```

### Create a connection point to GitHub
```Bash
	git remote add <point-name> <url-to-repository-in-github>
```
### To see de connection point created
```Bash
	git remote -v
```
### To Upload de local Repository to online Repository
```Bash
	git push -u <point-name> <name branch>
	git push

#If the Repository has changes and you dont have them in your local repository
#That generates an error, to solve this use de following commands

	git pull --allow-unrelated-histories <point-name> <branch>
# and to you will use push normally, use the following command
	git push --set-upstream  <point-name> <branch>

```