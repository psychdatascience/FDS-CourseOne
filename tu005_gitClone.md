## Cloning a GitHub Repository to Your Local Machine

### Objective: By the end of this exercise, you'll have a copy of your GitHub repository on your local computer and be set up to start using Git.

### Prerequisites: 
- Have a GitHub account.
- Have a repository on GitHub you wish to clone (you can use your Simpsons one from the last homework).
- Have Git installed on your computer.
If you have a relatively new computer, it should already have git on it. If not – and we'll find out pretty quickly! – we can download and install it from [download and install Git](https://git-scm.com/downloads).

---

### 1. Access the Repository on GitHub

- Navigate to GitHub at [https://github.com/](https://github.com/).
- Log in to your account if you're not already logged in.
- Go to your repository's main page.

---

### 2. Get the Repository URL

- On the main page of your repository, you'll find a button labeled **"Code"** with a dropdown arrow (the green button over towards the right, not the `<> Code` tab on the upper left).
- Click on this button. You'll see a URL (it should end in `.git`).
- Copy this URL. You'll use it to tell Git which repository you want to clone.

---

### 3. Open the Terminal

- **For older Windows users:** (the Windows version, not you) Search for "Git Bash" or "Command Prompt" from the Start menu and open it.
  
- **For macOS, recent Windows, and Linux users:** Open the "Terminal".

---

### 4. Navigate to the Directory Where You Want to Clone the Repository

- Use the `cd` command to navigate to your desired location. For example, if you want to navigate to a directory called "projects" in your home directory, you'd type:

  ```
  $ cd ~/projects
  ```
*A note on file organization: Some people prefer to have a "git" or "GitHub" folder under their home folder and keep each repo in there (each repo will have its own folder). Others might prefer to have, for example, "R_Projects" and "Python_Projects" directories in their home directory, and have the corresponding repos in there. How you organize your files is up to you, but the keyword is **organize**! The more organized you are now, the more future you will love past you (who is currently current you – isn't time travel fun?).*

---

### 5. Clone the Repository

- Use the `git clone` command followed by the URL you copied from GitHub:

  ```
  $ git clone [URL]
  ```

  Of course, replace `[URL]` with the actual URL you copied. For example:

  ```
  $ git clone https://github.com/lkcormack/i-hate-statistics.git
  ```

---

### 6. Confirm the Repository Has Been Cloned
The cloning operation will have created a new directory in the directory from which you did the `git clone ...`.
- Navigate into the newly cloned directory. For example:

  ```
  $ cd Documents/GitHub/i-hate-statistics
  ```

- Now, if you run the `ls` command (or perhaps `dir` on Windows), you should see any files or directories that were in your GitHub repository.

  ```
  $ ls
  ```
If you do an
  ```
  $ ls -a
  ```
you will see that there is a hidden `.git` folder in your repo. This is where the magic happens. **Do not touch!***

---

### 7. Set Up Your Identity (Only if it's your first time using git)

- To ensure that your commits are properly attributed to you, set up your git identity. Replace `Your Name` with your actual name and `youremail@example.com` with your email:

  ```
  $ git config --global user.name "Your Name"
  $ git config --global user.email "youremail@example.com"
  ```

---

### Conclusion: You've successfully cloned a repository from GitHub to your local machine! You're now ready to start making changes, committing them, and eventually pushing them back to GitHub.

---
