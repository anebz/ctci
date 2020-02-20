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
