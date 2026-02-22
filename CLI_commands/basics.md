# CLI (Command Line Interface)

## Explanation :
- CLI is a text-based interface where you type commands to interact with your computer , instead of using the GUI(Graphical user interface)
- It is mostly used for running programs , managing files , networking and automation 
- For example , terminal in Linux and Cmd in Windows 

## How it Works :
- you type a command like mkdir , ls , touch , ping 
- System Executes it and we see output in the Screen 

## Need For CLI :
- Faster than GUI for many tasks 
- Provides **Access to Advances features** not always available in GUI


## Example 

<pre>
hello
├── five
│   └── six
│       ├── c.txt
│       └── seven
│           └── error.log
└── one
    ├── a.txt
    ├── b.txt
    └── two
        ├── d.txt
        └── three
            ├── e.txt
            └── four
                └── access.log</pre>


- As you can see this is a folder structure which have files and folder in it recursively 
- As if we wanted to make the structure in GUI it would take a lot of time
- so we talk to computer by typing commands to tell our computer what to do 



# File & Folder Management Commands

## Listing Files & Folders

| Command | Meaning                 | What it does                                   | Example |
| ------- | ----------------------- | ---------------------------------------------- | ------- |
| `ls`    | list                    | Shows files and folders in current directory   | `ls`    |
| `ls -l` | list (long)             | Shows detailed list (permissions, size, owner) | `ls -l` |
| `ls -a` | list (all)              | Shows all files including hidden ones          | `ls -a` |
| `pwd`   | print working directory | Shows current directory path                   | `pwd`   |

## Creating Files & Folders 

| Command          | Meaning                 | What it does           | Example                  |
| ---------------- | ----------------------- | ---------------------- | ------------------------ |
| `mkdir folder`   | make directory          | Creates a new folder   | `mkdir notes`            |
| `mkdir -p a/b/c` | make parent directories | Creates nested folders | `mkdir -p one/two/three` |
| `touch file.txt` | touch                   | Creates an empty file  | `touch file.txt`         |


## Navigating Between Folders
| Command     | Meaning               | What it does           | Example       |
| ----------- | --------------------- | ---------------------- | ------------- |
| `cd folder` | change directory      | Move into a folder     | `cd Projects` |
| `cd ..`     | change directory (up) | Move to parent folder  | `cd ..`       |
| `cd ~`      | home directory        | Move to home directory | `cd ~`        |



## Viewing File Content

| Command     | Meaning     | What it does               | Example         |
| ----------- | ----------- | -------------------------- | --------------- |
| `cat file`  | concatenate | Displays full file content | `cat notes.txt` |
| `head file` | head        | Shows first 10 lines       | `head file.txt` |
| `tail file` | tail        | Shows last 10 lines        | `tail file.txt` |
| `less file` | less        | Scrollable file view       | `less file.txt` |

## Copying & Moving Files/Folders 

| Command           | Meaning          | What it does     | Example              |
| ----------------- | ---------------- | ---------------- | -------------------- |
| `cp src dest`     | copy             | Copies a file    | `cp a.txt b.txt`     |
| `cp -r dir1 dir2` | copy recursively | Copies a folder  | `cp -r one two`      |
| `mv src dest`     | move             | Moves or renames | `mv old.txt new.txt` |


## deleting Files & Folders 

| Command        | Meaning            | What it does              | Example          |
| -------------- | ------------------ | ------------------------- | ---------------- |
| `rm file`      | remove             | Deletes a file            | `rm test.txt`    |
| `rm -r folder` | remove recursively | Deletes folder & contents | `rm -r demo`     |
| `rm -i file`   | interactive remove | Asks before deleting      | `rm -i file.txt` |

## Searching Inside Files 

| Command             | Meaning            | What it does            | Example                  |
| ------------------- | ------------------ | ----------------------- | ------------------------ |
| `grep "text" file`  | global regex print | Finds text inside file  | `grep "error" log.txt`   |
| `grep -i text file` | ignore case        | Case-insensitive search | `grep -i hello file.txt` |


---
Yeah this commands will do the work for now

To Understand the Commands better we try to make the above tree structure 

1. **Create the Above directory structure. (Create empty files where necessary)**
     - Step 1: create the Root Folder
       - mkdir hello
       - cd hello
     - Step 2: Create the folder structure
       - mkdir -p five/six/seven
       - mkdir -p one/two/three/four
      - *(mkdir -p creates parent folders automatically)*
     - Step 3: Create the files
       - touch five/six/c.txt
       -  touch five/six/seven/error.log
       -  touch one/a.txt
       -  touch one/b.txt
       - touch one/two/d.txt  
       - touch one/two/three/e.txt
       - touch one/two/three/four/access.log
     - Step 4: Verify the Structure 
       - tree hello
2. **Add the following content to a.txt**
   
     *Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others*

     - echo " *your Text here* " >> a.txt
3. **Rename the one directory to uno**

   - *mv oldname newname*
   - mv one uno

4. **Move a.txt to the two directory**

    - *mv filename destinated_Folder*
    - mv uno/a.txt uno/two  
  


  

    






















  

