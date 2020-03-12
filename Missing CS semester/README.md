# [The Missing Semester of your CS education](https://missing.csail.mit.edu/)

## 1. [The shell](https://missing.csail.mit.edu/2020/course-shell/)

Create new file:

```bash
touch hello.txt
```

Write to new file / delete everything and write new:

```bash
echo 'my_string' > hello.txt
```

Append to file

```bash
echo 'my_string' >> hello.txt
```

To write two commands at the same time, use `|`. Also so that the output of the first command is the input to the second.

Write multiline string:

```bash
echo -e "Hello \nWorld \n" >> greetings.txt
```

Given a file with content:

```bash
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

Make it executable and execute it

```bash
chmod +x my_file
./my_file
```

[Stackoverflow info](https://askubuntu.com/a/229592):

> Generally, using ./filename.sh specifies a file in the current directory and using filename.sh specifies a file in the current directory or any directory of PATH. The first usage removes any uncertainty as to which file is accessed. In this case, you are attempting to execute the script with bash or another interpreter (by virtue of assumed #!/bin/bash as first line in your script) just by entering the filename. This usage requires the directory is specified. Alternatively, you can try bash filename.sh which seems to work with unspecified directory.

To find in file:

```bash
grep my_string file.txt
```

Run script, find string in string and output to file

```bash
./semester | grep 'my_string' > last-modified.txt
```

Use `grep -o` to display only matched pattern, `grep -P` for regex. [See stackoverflow](https://unix.stackexchange.com/a/13472)

## 2. [Shell tools and scripting](https://missing.csail.mit.edu/2020/shell-tools/)

### 2.1. Shell scripting

Add text to each file in directory, capture many files at the same time:

```bash
cp /path/to/project/{foo,bar,baz}.sh /newpath
mv *{.py,.sh} folder
```

### 2.2. Shell tools

```bash
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '**/test/**/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'

# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec convert {} {.}.jpg \;
```

`find` finds files/filenames, to find content inside files use `grep`. Some of the flags include `-C` for getting context lines around it, or `-v` for inverting the result, getting those lines that don't match the pattern. `-R` for recursively iterating in directories.

Alternatives like `rg` expand the capabilities of `grep -R` by ignoring .git files, etc.

```bash
# Find all python files where I used the requests library
rg -t py 'import requests'
# Find all files (including hidden files) without a shebang line
rg -u --files-without-match "^#!"
# Find all matches of foo and print the following 5 lines
rg foo -A 5
# Print statistics of matches (# of matched lines and files )
rg --stats PATTERN
```

> Finding shell commands

```bash
# find shell commands where you used apt
history | grep apt
```

Another trick is Ctrl+R, you can insert a subtring to find matching shell commands. By pressing Ctrl+R again, you can iterate through them. Tools for seeing history-based autosuggestions: [zsh](https://github.com/zsh-users/zsh-history-substring-search).

> Navigating directories

You can use [fasd](https://github.com/clvv/fasd) to autojump to common directories that you visit often.

To list all files in a directory in

* human readable
* show hidden
* print details
* sort by date

, do `ls -halt`.
