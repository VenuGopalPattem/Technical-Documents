# Practice Dril 2  

## Flags

**What is a Flag?**

- Flags are **options added to commands** to control or modify how that command behaves.
- In simple terms, it tells **how** to run a command, **not what** to run.
- **Syntax:**
```bash
command -flag arguments
```
  - **Eg** : `ls -l`
    - `ls` → list files
    -  `-l` → show detailed view
  
**Importance**
- It Makes the command more

| Benefit | Command Example | Explanation |
|---------|----------------|------------|
|  More Powerful | `ls -a` | Shows hidden + visible files (Standard `ls` only shows visible). |
|  More Precise | `rm -i file.txt` | Asks for confirmation before deleting (Standard `rm` deletes instantly). |
|  Efficient | `grep -i error log.txt` | Ignores case to match both "Error" and "error" in one go. |



  **Some of the Imp Flags**

| Priority | Flag | Name / Meaning | What it Does | Example |
|---------|------|---------------|--------------|---------|
| 1 | `--help` | Help | Shows available options | `ls --help` |
|  2 | `-h` | Human-readable / Help | Shows sizes in KB/MB/GB | `ls -lh` |
|  3 | `-a` | All | Shows hidden files | `ls -a` |
|  4 | `-l` | Long listing | Shows detailed info | `ls -l` |
|  5 | `-r` | Recursive | Works on dirs recursively | `rm -r dir` |
|  6 | `-i` | Interactive | Asks before action | `rm -i file` |
| 7 | `-f` | Force | Forces operation | `rm -f file` |
|  8 | `-v` | Verbose | Shows progress | `cp -v a b` |
|  9 | `-n` | Number | Limits output | `head -n 5 file` |
|  10 | `-o` | Output | Writes to file | `curl -o a.html URL` |
|  11     | `-d` | Directory        | Treats directories as files            | `ls -d */`                |
|  12     | `-p` | Preserve / Port  | Preserves properties or specifies port | `cp -p file1 file2`       |
|  13     | `-e` | Enable / Execute | Enables feature or executes command    | `bash -e script.sh`       |
|  14     | `-w` | Whole word       | Matches exact words                    | `grep -w "error" log.txt` |
|  15     | `-c` | Count            | Counts occurrences                     | `wc -c file.txt`          |



## Pipes
- **What is a Pipe**

  - A Pipe connects the command
  - It takes the output of the left command and feeds it as input to the right command

  **Eg**: <pre>`Command1 | command2`  
                  output → input </pre>

- **Importance of pipe**
  - Without pipes:

    - You’d need temp files

    - More commands

    - Slower workflow

  - With pipes:

    - One-liners

    - Faster

    - Cleaner

    - Powerful filtering
  - **Eg** : <pre> ls | grep py</pre>
  
- What happens:

        1. ls → lists files

        2. | → sends that list forward

        3. grep py → keeps only names containing py
   
        4. So it displays only py files in that directory 

# Exercise 

1. **Download the contents of "Harry Potter and the Goblet of Fire" using the command line**
   
   - Step 1: Use `curl` to download the book
     - ```bash
       curl -o goblet_of_fire.txt <your link>
       ```

   - Step 2: Verify the file exists
     - ```bash
       ls -l goblet_of_fire.txt
       ```

2. **Print the first three lines of the book**
   
   - Step 1: Use `head` to get first 3 lines
     - ```bash
       head -n 3 goblet_of_fire.txt
       ```


3. **Print the last 10 lines of the book**
   
   - Step 1: Use `tail` to get last 10 lines
     - ```bash
       tail -n 10 goblet_of_fire.txt
       ```



4. **Count how many times "Harry" occurs in the book**
   
   - Step 1: Use `grep` and `wc -l`
     - ```bash
       grep -o -i "Harry" goblet_of_fire.txt | wc -l
       ```



5. **Count how many times "Ron" occurs in the book**
   
   - Step 1: Use `grep` and `wc -l`
     - ```bash
       grep -o -i "Ron" goblet_of_fire.txt | wc -l
       ```


6. **Count how many times "Hermione" occurs in the book**
   
   - Step 1: Use `grep` and `wc -l`
     - ```bash
       grep -o -i "Hermione" goblet_of_fire.txt | wc -l
       ```

7. **Count how many times "Dumbledore" occurs in the book**
   
   - Step 1: Use `grep` and `wc -l`
     - ```bash
       grep -o -i "Dumbledore" goblet_of_fire.txt | wc -l
       ```


8. **Print lines 100 through 200 in the book**
   
   - Step 1: Use `sed` to print a range of lines
     - ```bash
       sed -n '100,200p' goblet_of_fire.txt
       ```


9. **Count the number of unique words (letters A-Z, a-z only, case-insensitive) in the book**
   
   - Step 1: Split words into lines, filter letters only, lowercase for case-insensitive counting
     - ```bash
       tr -c 'A-Za-z' '\n' < goblet_of_fire.txt | tr 'A-Z' 'a-z' | sort | uniq | wc -l
       ```

     - *(Steps explained:)*  
       - `tr -c 'A-Za-z' 'n'` → split all letters-only words into separate lines  
       - `tr 'A-Z' 'a-z'` → convert uppercase to lowercase for case-insensitive counting  
       - `sort | uniq` → remove duplicates  
       - `wc -l` → count total unique words








