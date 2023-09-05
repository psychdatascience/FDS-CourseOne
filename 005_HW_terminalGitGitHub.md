---

## **Homework on the Terminal, Git, and GitHub**

### Objective: Cover the basics of using GitHub, git (from the terminal), and keeping a repo synched.

---

### **The Homework:**
Let's go through the whole basic workflow for maintaining a repo. Try to do this with as little help as possible (of course you can peek at a cheat sheet if you need to). 

Note: We're making some "junk" repos while we learn. You can delete them once they've been checked so they don't clutter up your GitHub world.

---

### 1. Make a new repo on GitHub
Try to do it without peeking at help. You've got this!

* make a new repo on GitHub. Call it [your name/nickname]GitHomework or similar.
  - use the MIT license
  - add a README
  - keep it public 
* edit the README file in some way
* save the file
* add a new file 
  - name it whatever you want, but give it a `.py` extension
  - add a line `print("whatever")` ("whatever" can be whatever)
* commit your changes

---

### 2. Clone the repo to your computer
Your new repo now only exists in the cloud. Let's pull it down to your computer's drive.

* open a terminal wherever you want the repo to go<sup>*</sup>
* clone the repo
* confirm everything worked with a quick `ls`, `cd`, and another `ls`

<sup>*</sup> *Mac users: you can open a terminal directly from a finder window by right-clicking the folder in the path bar.*

### 3. Edit the repo
Let's add a new file!

* make a new `.md` file using `touch`
* add a heading and some body text to the file (probably easiest to just use `nano` or `micro` or whatever, but there are free markdown editors available such as Markdown Pro or Markdown Edit)
* save the file (important step!)

### 4. Commit the changes and push them up to GitHub
It ain't worth – slit? skit? swit? – if you don't commit!

* stage (add) your changed file
* commit the changes with a terse yet witty commit message (the witty is optional)
* see what's up with a `git status`
* push your changes up to GitHub
* check the status again - `git status` never wears out, it's like the Energizer Bunny!

---

### 5. Make another change on GitHub
We know, we know, you know how to do this now, but we need something to fetch to your local computer!

* add the following to your .py file
  ```
  a = 40 + 2
  print("The answer (to everything) is ", a)
  ```
* save (commit) the change  
**Pro Tip:** *The standard save the shortcut, `cmd s`, works; it pops up the commit window without you having to scroll up to the commit button.*

---

### 6. Pull the remote changes down to your local computer
Let's complete the whole cycle by fetching and pulling. 

* go back to the terminal that has your repo as its current directory (or open a new one there)
* check the status
* do a `git fetch` to fetch any changes made to the remote (GitHub) repo
* check the status (yes, again!)
* pull the actual changes (`git fetch` only gets a description of the changes, `git pull` actually gets them for you)
* check the status one last time!

---

Summary: That's a run-through of the most common steps in a git/GitHub workflow – probably 90% or more of a standard project workflow. I wouldn't call ourselves git ninjas or gitmasters or whatever just yet, but we're progressing above the git bunny level for sure!

For credit, just submit 1) the link to the GitHub repo and 2) a screenshot of an `ls` at the local repo.

Bonus fun: In the terminal window that is "in" your repo, type `python [yourfile.py]` where [yourfile.py] is whatever you named your .py file in the repo. You should see the answer printed in your terminal!
