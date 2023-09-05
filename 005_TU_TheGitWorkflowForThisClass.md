## Learn About the Git Workflow that will be used in this class

Learning Goals:

 * Learn and practice with the `git` workflow used by this class
 * Create a repository on GitHub.com.
 * Clone the repository locally on your computer.
 * Copy a file into the new local repository
 * Add the changes to the stack of changes in the local git repository.
 * Commit the changes to the record of the local repository.
 * Push the local repository to GitHub.com

### 0. Overview of the Canvas->Git->GitHub->Canvas workflow we will use.

We will now go over the steps necessary to update, work with, and report on the tutorials and exercises for the remainder of the semester. Every week we (Dr. Cormack and Pestilli) will provide one or more files to download from a "module" on Canvas. These files will need to be saved locally on your computer. The files will be saved inside a `git` repository that we will create today and that will be used for the rest of the semester. The weekly files will be added to the repository, used for the tutorials in class, or the homework, and then pushed to GitHub. For each weekly file, you will submit 
 
  - a PDF via Canvas (by uploading a PDF of your local tutorial with executed cells or completed homework)
  - a URL of your repository on GitHub.com pointing to the tutorial/homework notebook.

### 1. Create the GitHub Repository we will use for this class.

Let's go over some of the steps from previous Tutorials and create a repository on GitHub.com. The repository will be named:
`YourEID_FDS1`.

#### Navigate to GitHub.com/yourUserName and Sign in to your account.

First, navigate to GitHub.com and *sign in*. 

[![This is a Video Reminder on How to Login on GitHub, if neeed](https://img.youtube.com/vi/KGLG-0VIEDM/0.jpg)](https://www.youtube.com/watch?v=KGLG-0VIEDM)

#### Create a repository: Using the Web User Interface (Web UI).

Next, create a new repository. Importantly, the name of the repository should match the following pattern: `YourEID_FDS1`, because that is the pattern we will use for the class. See this is the URL to my repo on GitHub: [https://github.com/francopestilli](https://github.com/francopestilli/fp4834_FDS1) 

[![This is a video showing how to create a new repository using the graphical interface on GitHub. The name of the repository is special as it matches the user's ID.](https://img.youtube.com/vi/qijRlJpBm9A/0.jpg)](https://www.youtube.com/watch?v=qijRlJpBm9A).

#### Clone the new repository from GitHub.com onto your local computer.

On your local computer, navigate to the root of your `git` repositories:

```
 cd ~
 cd MyGitRepos
```

The command that will allow the repository online to be copied locally on your computer while maintaining an invisible link to your online repository living on GitHub is `clone`:

```
git clone https://github.com/yourUserName/yourEID_FDS1 
```

The command will make a copy of the online repository on the current directory on your computer. So let's check this. You can show your current directory `pwd`. You can see all files and folders in your current using `ls -l`. We can navigate to the new repository folder `yourUserName` using `cd yourUserName`. 

[![This video shows how to clone a repository already existing on GitHub.com using terminal on Mac OSX.](https://img.youtube.com/vi/G931KZx4Rhc/0.jpg)](https://www.youtube.com/watch?v=G931KZx4Rhc).

### 2. Download the file needed from Canvas to your local git repository.

We want to navigate to Canvas, and then:

* find the module for this week,
* find the file to download (call it `ThisWeekTutorial.ipynb`)
* download the file.
* move the file to `~/MyGitRepos/YourEID_FDS1`

[Hint. You can move the file using a terminal and the command `mv`.]

### 3. Add the file to your local git repository.

After downloading and moving the `ThisWeekTutorial.ipynb` inside your git repository for the class: `~/MyGitRepos/YourEID_FDS1` we will add it to the git repository. Open a terminal and follow the next steps.

#### Add the File to the git "Staging Area"

In a terminal, navigate to your Git repositories folder and inside the folder for this class

```
$ cd ~/MyGitRepos/YourEID_FDS1
```

Check the status of the repository (it should have a new file, just copied into it):

```
$ git status
```

Follow git's advice and add `ThisWeekTutorial.ipynb`.

```
$ git add ThisWeekTutorial.ipynb
```

Do a git status again for verification - git status is your friend!

```
$ git status
```

(We won't do a git status all the time once you get better at `git` but, for now, it'll help us learn).

### 4. Commit the File

Commit the staged changes with a message.

```
$ git commit -m "Created ThisWeekTutorial.ipynb"
```

### 5. Make Changes to index.html

Open `ThisWeekTutorial.ipynb` using `Jupyter`.

### 6. Work on your tutorial/assignment 

[This will Make changes to `ThisWeekTutorial.ipynb`]

* Open `ThisWeekTutorial.ipynb` using `Jupyter`
* Follow the tutorial and execute the cells

### 7. Check the Status Again

Note the changes in your repository.
```
$ git status
```

You should see `ThisWeekTutorial.ipynb` as modified. Remember, git status is your friend!

### 8. Stage and Commit the Changes

Add the modified file to staging and then commit it.

```
$ git add ThisWeekTutorial.ipynb
$ git commit -m "Added content to ThisWeekTutorial.ipynb"
```

### 8. Push to the Remote Repository
Ensure your local changes are synchronized with the remote repository (GitHub).

```
$ git push
```

That's it, you're synched up!

Go to your GitHub page, and you should see `ThisWeekTutorial.ipynb` in your `YourEID_FDS1` repo.

### 9. Submit the URL of the tutorial

Every week you will need to submit the URL to your repository with the tutorial done, or the homework completed. To do so, copy and paste the URL of your tutorial from your GitHub into the appropriate location on Canvas. 

Here is the URL of my tutorial: https://github.com/francopestilli/fp4834_FDS1/blob/main/myFirstTutorial.ipynb

### 10. Print the tutorial and upload the PDF 

Finally, we ask that you submit your notebook as a PDF file by uploading it on Canvas following the appropriate Assignment inside the model.



