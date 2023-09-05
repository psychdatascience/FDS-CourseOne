
---

## **Basic Git Functionality Exercise**

### Objective: Familiarize yourself with basic Git commands and understand the flow of changes from your local machine to a remote repository – and back.

---

### **The Plan:**
You want a simple webpage to tell the world who your favorite Simpsons character is. You'll 

* create a basic HTML file
* put in some content 
* save the file
* add the file to the git staging area
* commit your changes
* push the changes to the remote repository on GitHub.
* make a change to the same file on GitHub
* pull those changes back to your local repo

---

### 1. Create a New File

- Open a terminal in the directory of the repo you cloned in the last exercise (the Simpsons repo).
- In the root of your cloned repository, create a new file named `index.html`.

  ```
  $ touch index.html
  ```

---

### 2. Check Git Status

- Always a good practice to check the status of your Git repository.

  ```
  $ git status
  ```

  You should see `index.html` as an untracked file, and a suggestion to add the file.

---

### 3. Add the File to the git "Staging Area"

- Follow git's advice and add `index.html`.

  ```
  $ git add index.html
  ```
- Do a git status again for verification - git status is your friend!

  ```
  $ git status
  ```
  (We won't do a git status all the time once you get better at git but, for now, it'll help us learn)
---

### 4. Commit the File

- Commit the staged changes with a message.

  ```
  $ git commit -m "Created index.html"
  ```

---

### 5. Make Changes to `index.html`

- Open `index.html` in a text editor of your choice.
  * on a mac, you can type `nano index.html` at the command line
  * on Windows, try `micro index.html`
  * you can also just open it in `notepad` (Windows) or `textedit` (Mac)

- Add the following basic HTML content (you can copy and paste - modify the title or body as you see fit):

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>My Simpsons Page</title>
  </head>
  <body>
      <h1>Welcome to My First Page!</h1>
      <p>My favorite Simpsons character is Maggie.</p>
  </body>
  </html>
  ```

- Save and close the file.

---

### 6. Check the Status Again

- Note the changes in your repository.

  ```
  $ git status
  ```

  You should see `index.html` as modified. Remember, `git status` is your friend!

---

### 7. Stage and Commit the Changes

- Add the modified file to staging and then commit it.

  ```
  $ git add index.html
  $ git commit -m "Added content to index.html"
  ```

---

### 8. Push to the Remote Repository

- Ensure your local changes are synchronized with the remote repository (GitHub).

  ```
  $ git push
  ```

That's it, you're synched up!

Go to your GitHub page, and you should see index.html in your Simpsons repo.

---

Aside: If you did your editing in nano or micro, you should be able to open your local copy of index.html in your web browser and see it displayed as a webpage!

---

### 9. Make a change on GitHub and then synch your local repo with the remote changes

For this step, you need to make a change directly on the GitHub repository. 

- Go to your repository on GitHub.
- Navigate to `index.html`.
- Click the pencil icon to edit the file.
- Add another paragraph in the <body> section:

  ```
  html
  <p>This is a change made directly on GitHub!</p>
  ```

- Hit the "Commit Changes..." button and commit the changes with the message: "Direct edit on GitHub."

---

### 10. Fetch and Pull the Changes

- On your local machine, fetch the changes.

  ```
  $ git fetch
  ```

  This command fetches the changes but doesn't merge them. Now that you've "fetched" the change, use `git status` to summarize
  ```
  $ git status
  ```
  Remember, `git status` is your friend!

- Now, `pull` the changes to merge them.

  ```
  $ git pull
  ```

  If you open `index.html` in a text editor on your local machine, you'll see the new paragraph you added on GitHub.

---

### Conclusion: Congratulations! You've just practiced creating, modifying, committing, and synchronizing files using Git and GitHub. That's the basic git/GitHub workflow in both directions! With these foundational skills, you're on your way to mastering version control!

---
