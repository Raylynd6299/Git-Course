# Git-Course

Tooos los archivos aqui escritos aparte del mismo README y el "git_manual.md", son usados como ejemplo

# Git-Manual
Esta informacion y más en el archivo [**git_manual.md**](./git_manual.md)
Esta extenso
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


# Do Commits #
```Bash
# Only commit
	git commit
# With message
	git commit -m "Message"
# Add all files and do commit with message
	git commit -am "Message"
```
