## This homework will ask you to practice the Git/GitHub Workflow that will be used in this class

### 0. Overview of the Canvas->Git->GitHub->Canvas workflow we will use.

We will now go over the steps necessary to update, work with, and report on the tutorials and exercises for the remainder of the semester. Every week we (Dr. Cormack and Pestilli) will provide one or more files to download from a "module" on Canvas. These files will need to be saved locally on your computer. The files will be saved inside a `git` repository that we will create today and that will be used for the rest of the semester. The weekly files will be added to the repository, used for the tutorials in class, or the homework, and then pushed to GitHub. For each weekly file, you will submit 
 
  - a PDF via Canvas (by uploading a PDF of your local tutorial with executed cells or completed homework)
  - a URL of your repository on GitHub.com pointing to the tutorial/homework notebook.

### 1. Download the Jupyter notebook from the Homework on Canvas

We want to navigate to Canvas, find the 005_HW_PracticeWithThisJupyterNotebook.ipynb notebook, and then download it.

### 3. Add the file to your local git repository.

After downloading and moving the `/005_HW_PracticeWithThisJupyterNotebook.ipynb` inside your git repository for the class: `~/MyGitRepos/YourEID_FDS1` we will add it to the git repository. Open a terminal and follow the next steps.

#### Add the File to the git "Staging Area"

In a terminal, navigate to your Git repositories folder and inside the folder for this class

```
$ cd ~/MyGitRepos/YourEID_FDS1
```

Check the status of the repository (it should have a new file, just copied into it):

```
$ git status
```

Follow git's advice and add `/005_HW_PracticeWithThisJupyterNotebook.ipynb`.

```
$ git add /005_HW_PracticeWithThisJupyterNotebook.ipynb
```

Do a git status again for verification - git status is your friend!

```
$ git status
```

(We won't do a git status all the time once you get better at `git` but, for now, it'll help us learn).

### 4. Commit the File

Commit the staged changes with a message.

```
$ git commit -m "Created /005_HW_PracticeWithThisJupyterNotebook.ipynb"
```

### 5. Make Changes to index.html

Open `/005_HW_PracticeWithThisJupyterNotebook.ipynb` using `Jupyter`.

### 6. Work on your tutorial/assignment 

[This will Make changes to `/005_HW_PracticeWithThisJupyterNotebook.ipynb`]

* Open `/005_HW_PracticeWithThisJupyterNotebook.ipynb` using `Jupyter`
* Follow the tutorial and execute the cells

### 7. Check the Status Again

Note the changes in your repository.
```
$ git status
```

You should see `/005_HW_PracticeWithThisJupyterNotebook.ipynb` as modified. Remember, git status is your friend!

### 8. Stage and Commit the Changes

Add the modified file to staging and then commit it.

```
$ git add /005_HW_PracticeWithThisJupyterNotebook.ipynb
$ git commit -m "Added content to /005_HW_PracticeWithThisJupyterNotebook.ipynb"
```

### 8. Push to the Remote Repository
Ensure your local changes are synchronized with the remote repository (GitHub).

```
$ git push
```

That's it, you're synched up!

Go to your GitHub page, and you should see `/005_HW_PracticeWithThisJupyterNotebook.ipynb` in your `YourEID_FDS1` repo.

### 9. Submit the URL of the tutorial

Every week you will need to submit the URL to your repository with the tutorial done, or the homework completed. To do so, copy and paste the URL of your tutorial from your GitHub into the appropriate location on Canvas. 

Here is the URL of my tutorial: [https://github.com/francopestilli/fp4834_FDS1/blob/main/myFirstTutorial.ipynb](https://github.com/francopestilli/fp4834_FDS1/blob/main//005_HW_PracticeWithThisJupyterNotebook.ipynb)

### 10. Print the tutorial and upload the PDF 

Finally, we ask that you submit your notebook as a PDF file by uploading it on Canvas following the appropriate Assignment inside the model. If you do not remember how to save a PDF from a Jupyter Notebook [here is a Video of how I do it on my Mac OSX computer using Google Chrome as a browser](https://youtu.be/B2SvTX4-RS8)

### 11. Excellent, you are done!

The above is the workflow we will use for every week and lecture. We will always give you a file (most often a Jupyter Notebook) and ask that you download it from Canvas, then add it to your local git repository, push it to the cloud, and submit both a URL pointing to the notebook under your GitHub account and a PDF of the tutorial with all the questions answered or exercises completed. Remember, we will use the same repository for the whole semester `YourEID_FDS1`, so keep good care of it and practice well!



