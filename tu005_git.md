
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
* pull those changes back to you local repo

---

### 1. Create a New File

- Open a terminal in directory of the repo you cloned in the last exercise (the Simpsons repo).
- In the root of your cloned repository, create a new file named `index.html`.

  ```
  $ touch index.html
  ```

---

### 2. Check Git Status

- Always a good practice, check the status of your Git repository.

  ```
  $ git status
  ```

  You should see `index.html` as an untracked file.

---

### 3. Add the File to Staging

- Add `index.html` to the staging area.

  ```
  $ git add index.html
  ```

---

### 4. Commit the File

- Commit the staged changes with a message.

  ```
  $ git commit -m "Add initial index.html file"
  ```

---

### 5. Make Changes to `index.html`

- Open `index.html` in a text editor of your choice.
- Add the following basic HTML content:

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>My First Page</title>
  </head>
  <body>
      <h1>Welcome to My First Page!</h1>
      <p>This is a basic Git exercise.</p>
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

  You should see `index.html` as modified.

---

### 7. Commit the Changes

- Add the modified file to staging and then commit it.

  ```
  $ git add index.html
  $ git commit -m "Add content to index.html"
  ```

---

### 8. Push to the Remote Repository

- Ensure your local changes are synchronized with the remote repository (GitHub).

  ```
  $ git push
  ```

  If you face an error (because changes have been made to the remote repository that you don't have locally), you'll have to `fetch` and `pull`. Since this is a basic exercise, we'll assume this doesn't happen. But it's something to be aware of in real-world scenarios!

---

### 9. Simulate a Scenario for `git fetch` and `git pull`

For this step, you need to make a change directly on the GitHub repository. 

- Go to your repository on GitHub.
- Navigate to `index.html`.
- Click the pencil icon to edit the file.
- Add another paragraph:

  ```html
  <p>This is a change made directly on GitHub!</p>
  ```

- Scroll down and commit the changes with the message: "Direct edit on GitHub."

---

### 10. Fetch and Pull the Changes

- On your local machine, fetch the changes.

  ```
  $ git fetch
  ```

  This command fetches the changes, but doesn't merge them.

- Now, pull the changes to merge them.

  ```
  $ git pull
  ```

  If you open `index.html` on your local machine, you'll see the new paragraph you added on GitHub.

---

### Conclusion: Congratulations! You've just practiced creating, modifying, committing, and synchronizing files using Git and GitHub. With these foundational skills, you're on your way to mastering version control!

---
