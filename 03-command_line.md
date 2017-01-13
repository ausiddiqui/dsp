# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `ls -lR` : lists the folder contents with details, looks into subfolders as well

> > `cat <filename>`: outputs the contents of the file into the terminal window without having to open it using an editor

> > `head -n <filename>`: outputs the first n lines of a file into the terminal Windows

> > `cp -R <dirname> <to_dirname>`: copies folder or renames it

> > `chown -R <user>:<group> <dirname>`: recursively changes the ownership and group of the directory and contents

> > `grep <text> <filename>`: searches for the text within a specified file

> > `rm -r <dirname>`: remove directories listed

> > `tar -zcvf <filename.tar.gz> <dirname>`: unzip zipped file to the specified directory

> > `less <filename>`: outputs the content of the file into the terminal with the ability to scroll through

> > `<command> >> <filename>`: outputs the results of the command on the left to the file on the right.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`: outputs the contents of a the current directory

> > `ls -a`: outputs the directory contents including hidden files

> > `ls -l`: outputs the directory contents in a list with details

> > `ls -lh`: outputs the directory contents in a detailed list with the appropriate unit suffixes for the size of the file

> > `ls -lah`: outputs the directory contents in a detailed list including hidden file and unit suffixes for the size of the files

> > `ls -t`: outputs the directory contents but sorts the order of listing them from most recently modified being shown first

> > `ls -Glp`: outputs the directory contents in a detailed list highlighting different filetypes by color and adding a '/' next to the name of directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -m`: directory contents as a comma separated list

> > `ls -lR`: lists subdirectory contents in detailed list view

> > `ls -d`: displays only the directories

> > `ls -r`: displays output in reverse order

> > 'ls -u': displays output by file access time

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > The xargs command can read space, tab, newline and end-of-file delimited strings from standard output and is able to carry out another command on these by using these as an argument. It is especially useful for batch processing or carrying out the same command on a group of files.

> > `find . -name "*.csv" -print0 | xargs -0 -I {} mv {} ~/data/csv`
