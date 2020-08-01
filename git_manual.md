# Git-Manual

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

# Do Commits #
```Bash
#Only commit
	git commit
#With message
	git commit -m "Message"
# Add all files and do commit with message
	git commit -am "Message"
```

# Travel in Time(Commits) or Branchs  #
```Bash
*Travel through commits*
	git switch -d <ID of commit>
*switch Branch*
	git switch <branch name>
*Create a Branch*
	git switch -c <branch>
*Merge in a new Branch
	git switch -m <Branch>
*Return to master branch and (HEAD) commit
	git switch -
	git switch master
```

