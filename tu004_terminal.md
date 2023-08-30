## Introduction to Basic Shell Commands

### Objective: 
This exercise will give you some more hands-on practice with the shell commands introduced in the previous reading. By the end of this exercise, you should be able to navigate your computer's file system, create, view, copy, and move files, and use wildcards.

---

### 1. Launch the Terminal

The terminal is where you'll enter shell commands. On most systems, you can find the Terminal application in the Applications menu or search for it. *Note: on Windows, the newest terminal application is now called "Terminal" – yay! – which replaces the older PowerShell and even older Console.* If you're on an older Windows machine, just substitute "PowerShell" or "Console" whenever we say "Terminal".

---

### 2. Navigating the File System
To navigate the file system, we need to be able to 

* see where we are – our current location in the file system
* see what's there – which files and directories are housed in the current directory
* jump around – change our current location to a new location in the file system

#### 2.1. `pwd` – Print Working Directory
The `pwd` command lets us see where we are. It will display the path down the file tree from the very top, "root", all the way down to your current location. (Your current directory, without the whole path, might be displayed in your prompt or in the title bar of your terminal window.)

- Type `pwd` and hit `Enter` (the "$" represents the terminal prompt, so don't type it). 
  ```
  $ pwd
  ```

  - What's displayed? (Rhetorical question, but make sure you understand what you are seeing.)
 
  Don't be afraid to use this often! There's no crime in using it everytime you change you current location, just to be sure!

#### 2.2. `ls` – List Files and Directories
The `ls` command will **l**i**s**t files and directories (folders) in your current directory. By default, it will list everything that's not a "hidden" file in a short format, listing only the names.

- Type `ls` and press `Enter`.
  ```
  $ ls
  ```

  - What do you see?
 
  The `ls` command has many options to filter what you see. Let's try some of them!

  - Try each of these in turn
    
  ```
  $ ls -l
  ```
  This lists the files and folders in "long" format, giving addtional information in each row. This will be useful later in your data science life but, now, not so much.

  ```
  $ ls -F
  ```
  This lists the files in **F**abulous format (actually, it's probably classi**F**y – sometimes developers just pick a letter that's available and unlikely to be used for anything else...). This tells you what each thing is by appending a special character. *Most usefully, it will put a backslash after directories.*

  ```
  $ ls -a
  ```
  This lists **a**ll the files in the current directory, including *hidden* files whose names beging with a ".", which tells the OS to not show them to people by default. These are files that regular users don't need to worry about, and should only be messed with if you are *sure* you know what you're doing!

You can specify multiple options at once just by tacking them together. So, yes, you can do 
  ```
  $ ls -aF
  ```
Awesome aF, right?

### 2.3. `cd` – Change Directory

- To navigate into a directory, use `cd [directory_name]`. If your want to jump into a directory that is in your current directory, you just type is name after `cd`. So, for example, if you have a "Documents" directory in your current folder, you can jump into it with:
  ```
  $ cd Documents
  ```
  Do another `ls -F`, pick a directory, and jump into it.

  - You can go back to the "parent" directory (the one that contains the current directory) using:
    ```
    $ cd ..
    ```
    Where ever you may roam, you can jump instantly back to your home directory using
    ```
    $ cd ~
    ```
    So "~" always means your home directory, ".." always means the parent directory. "." means the current directory, but you won't need that much.

---

### 3. Manipulating Files

#### 3.1. `touch` – Create a New File

- Type `touch my_file.txt` and hit `Enter`.
  ```
  $ touch my_file.txt
  ```

  - Use `ls` to see if the file was created.

#### 3.2. `cp` – Copy a File

- Copy `my_file.txt` to a new file named `my_copied_file.txt`:
  ```
  $ cp my_file.txt my_copied_file.txt
  ```

  - Use `ls` to see both files.

#### 3.3. `mv` – Move or Rename a File

- Rename `my_copied_file.txt` to `my_renamed_file.txt`:
  ```
  $ mv my_copied_file.txt my_renamed_file.txt
  ```

  - Use `ls` to confirm the change.

---

### 4. Wildcards

#### 4.1. Using `*` Wildcard

- The `*` wildcard matches any number of characters.
- Create a few more files for this example:
  ```
  $ touch file1.txt file2.txt file3.doc
  ```

  - List only the `.txt` files:
    ```
    $ ls *.txt
    ```

---

### 5. Clean Up

- Let's clean up the files we created.
  ```
  $ rm my_file.txt my_renamed_file.txt file1.txt file2.txt file3.doc
  ```

  - Use `ls` to make sure the files are gone.

---

Conclusion:

Well done! You've now taken your first steps into the world of shell commands. With practice, these commands will become second nature to you. Remember, the terminal is a powerful tool, and the commands you've learned today are just the tip of the iceberg!

---

