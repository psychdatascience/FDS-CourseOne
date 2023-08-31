---

## **Homework on the Terminal, Git, and GitHub**

### Objective: Cover the basics of using GitHub, git (from the terminal), and keeping a repo synched.

---

### **The Homework:**
Let's go through the whole basic workflow for maintaining a repo. Try to do this with as little help as possible (of course you can peek at a cheat sheet if you need to). 

Note: we're making some "junk" repos while we learn. You can delete them once they've been checked so they don't clutter up your GitHub world.

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
  - give it a `.py` extension
  - add a line `print("whatever")` ("whatever" can be whatever)
* commit your changes

---

### 2. Clone the repo to your computer
Your new repo now only exists up in the cloud. Let's pull down to your computer's drive.

* open a terminal where ever you want the repo to go^*^
* clone the repo
* confirm everything worked with a quick `ls`, `cd`, and another `ls`

### 3. Edit the repo
Let's add a new file!

* make a new `.md` file using `touch`
* add a heading and some body text to the file (probably easiest to just use `nano` or `micro` or whatever, but there are free markdown editors available such as Markdown Pro or Markdown Edit)
* save the file (important step!)

### 3. Commit the changes and push them up to GitHub
It ain't worth – slit? skit? swit? – if you don't commit!

* stage (add) your changed file
* commit the changes with a terse yet witty commit message (the witty is optional)
* see what's up with a `git status`
* push your changes up to GitHub
* check the status again - `git status` never wears out, it's like the Energizer Bunny!

