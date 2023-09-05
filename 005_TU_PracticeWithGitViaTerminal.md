## Let's make something helpful with git/GitHub!

#### Practice using Git and GitHub via the terminal

Learning Goals:

 * Create a repository on GitHub.com.
 * Clone the repository locally on your computer.
 * Make changes to a file inside the repository.
 * Add the changes to the stack of changes in the local git repository.
 * Commit the changes to the record of the local repository.
 * Push the local repository to GitHub.com
 * (Handle advanced authentication features on GitHub, if necessary.)

Prerequisites:

* Internet access on Linux or Unix based computer (or Windows, especially with PowerShell)
* Git Installed
* A GitHub account and the ability to create a GitHub Repo, i.e., the previous tutorials

### 1. A reminder for version control.

In this tutorial, we will practice performing some more operations using `git` and the command line interface, the shell, on your local computer. From now on, we will assume that `git` is installed on your computer.

Just as a general reminder. Version control is a method to keep track of files and folders for a computer file system. We all have used some sort of version control. For example, I like to save files on my computer with the following naming convention `year-collaborator-project-some_details.ext`, say `2022-larry-datascience-to_do_list.pdf`. I like to save files in folders also organized by date: `/Users/francopestilli/UTAustin/Teaching/2023/Fall/DataScience/`. I then update the same file or make new versions of the file every year. When I update files and folders I change the year in their name. Many of us have performed similar operations, manually, and many of us have encountered the challange of developing a good way to keep track of file names and being more or less diligent in updating the file names. A version control system is a way to use computers to do what humans are not very good at keeping track of small changes, updating files as they are modified, and remembering to update records.

### 2. Set up a MyGitRepos Folder to keep all your repositories.

Developers, Data Scientists, and Scientists alike prefer to keep their file systems well organized. One simple strategy to keep all your git repositories organized is to create a folder on the home directory of your file system and to use that folder to keep all your `git` repositories. For example, on my computer, I created a folder called: `/Users/francopestilli/MyGitRepos/`.

Let's make a folder where you will keep all the files for this class. Open a terminal and navigate to your home directory. 

Type the following in your terminal:

```
 cd ~
```

Check that you are now in the home directory of your current user:

```
pwd
```

Now let's create a folder where we will keep the git repository for this class (and any other file you might like to keep). We will call the folder `MyGitRepos`:

```
 mkdir -v MyGitRepos
```

Check that the folder was created:

```
ls
```

Great, you should now have the folder we will use to store all the future git repositories for this class. [It is fine to make the folder in a different location, or call it differently, but we will use the above standard. We will expect a folder in your home directory called MyGitRepos.]

### 3. Practice creating and cloning a new repository.

We will now create a new repository, and edit files and directories in it, perform commits via the terminal. 

To practice using git via the terminal, we will create your own GitHub Resume! So that you will also improve your online Data Science presence. [GitHub recently allowed users to create a repository that can be used as the landing page for your GitHub page.](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/about-your-profile) A sort of CV (Resume) that will display as people navigate to your GitHub account. Data science geeks will like the idea of having a slick setup and appealing GitHub page as that page is your passport to the world of data science!

So, first, let's repeat some of the steps from a previous Tutorial and create a repository on GitHub.com.

#### Navigate to GitHub.com/yourUserName and Sign in to your account.

First, navigate to GitHub.com and *sign in*. 

[![This is a Video Reminder on How to Login on GitHub, if neeed](https://img.youtube.com/vi/KGLG-0VIEDM/0.jpg)](https://www.youtube.com/watch?v=KGLG-0VIEDM)

#### Create a repository: Using the Web User Interface (Web UI).

Next, create a new repository. Importantly, the name of the repository should *match* your GitHub user ID, in my case the repository will be named `francopestilli`, because that is my user ID on GitHub, see this is the URL to my user on GitHub: https://github.com/francopestilli 

[![This is a video showing how to create a new repository using the graphical interface on GitHub. The name of the repository is special as it matches the user's ID.](https://img.youtube.com/vi/qijRlJpBm9A/0.jpg)](https://www.youtube.com/watch?v=qijRlJpBm9A).

After all these steps, you can navigate to your GitHub Resume Repository: https://github.com/yourUserName/yourUserName (hint: change the URL to use your real user name), you will see something like the following:

<img width="1393" alt="YourGitHubResumeRepo" src="https://user-images.githubusercontent.com/2119795/151894081-ecb31b0e-9556-4911-a37d-5326db550f0b.png">

#### Clone the new repository from GitHub.com onto your local computer.

Next on your local computer, navigate to the root of your `git` repositories:

```
 cd ~
 cd git
```

The command that will allow the repository online to be copied locally on your computer while maintaining an invisible link to your online repository living on GitHub is `clone`:

```
git clone https://github.com/yourUserName/yourUserName 
```

The command will make a copy of the online repository on the current directory on your computer. So let's check this. You can show your current directory `pwd`. You can see all files and folders in your current using `ls -l`. We can navigate to the new repository folder `yourUserName` using `cd yourUserName`. 

[![This video shows how to clone a repository already existing on GitHub.com using terminal on Mac OSX.](https://img.youtube.com/vi/G931KZx4Rhc/0.jpg)](https://www.youtube.com/watch?v=G931KZx4Rhc).

### 4. Edit your repository.

We want to edit the README.md file that came with the repository. While doing this, we will temporarily put the terminal aside (do not close it, just minimize the window). We will then use any editor to edit the README.md file that came with the repository we just cloned. 

Pick your editor of choice, edit the README.md file, and let's add your First Name, Middle initials, and Family name as the Title header, after that let's add a tag-line that can give a quick sense of who you are for example *I am a professor at The University of Texas at Austin interested in Psychology, Neuroscience and Data Science.* After that let's write a short biography. Write something short about your background, for example, I would write: 

*I work in a Public University because I believe in science and education. I like to think that by teaching young minds how to think critically and how to use cutting-edge tools, like coding, we can make the world a better place. It is not a simple task, but I believe we can.* 

Finally, finish editing, save, and close your editor. Now we are ready to make our `commit`. 

First, let's learn how to take a look at the status of your local repository. Let's go back to the terminal, navigate to the new folder we just cloned, and check the status of the repository:

```
cd /Users/francopestilli/git/yourUserName
git status
```

Below is a snapshot of what the command `git status` returned on my computer after editing the README.md:

```
(base) francopestilli@francos-mbp francopestilli % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md
```

As you can see `git` has detected changes to the `README.md` file. Let's analyze the output above:

  - `On branch main` This means that you are currently working on the main development thread for this repository. Git allows "branching" (just like a tree branch). This means that you can create a copy (a `branch`) of the repository that diverges from the principal (`main` branch). Generally, branches are "merged" back into the main branch after a certain development goal is achieved. [Here is some additional reading material to understand basic branching](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).
  - `Your branch is up to data with origin/main` This means that the files in your local copy of the repository and the main branch you are currently working on are the same as the versions of the files committed to the cloud version of the repository, the `origin` is, in a nutshell, the term used here to refer to the cloud-hosted copy of the repository, so the files on GitHub.com.
  -  `Changes not staged for commit:` ... `modified:   README.md` This block of text, says that a file (`README.md`) on your local version of the repository has been modified and suggests a way to `restore` the file to the original version (the version still on `origin`) or a way to `add` the changes to the wanted changes that will need to be added to the `origin` when the next `commit` is performed.

### 5. Commit the changes and push to `origin`.

Next, we will want to close the loop of the process that will take our local changes to README.md to be accepted and recorded as the official, newest version of the file.
  - The process of accepting or promoting the local version of a file as the current version is called a `commit`. We commit to a change when we think it is a good change, that should be kept.
  - The process of synching the local files with the files in the cloud version of the repository is called a `push`, we push to the cloud. We `pull` from the cloud to a local version of a repository. 

Because `git` is a distributed version-control system there are often multiple ways to do things. hereafter we will show one convenient way to perform a commit and a push and sync all the files but there can be alternative ways to achieve the same state.

#### Commit the file changes to your local repository

Above, when we run the command `git status`, git suggested to use the command `add` to add the changes to README.md to the stack of changes to be committed to the local repository. That would look like the following:

```
git add README.md
git commit -m "I started editing README.md and added some basic information about myself."
```

The above would first add the changes detected by git to README.md and then commit the changes to the local copy of the repository (and add the mandatory commit message using the option `-m`). After that, the files will be changed on your local computer, but not yet pushed to the cloud, or better to `origin`. So, if your harddrive were to die or you would spill a cup of coffee on your computer you would risk losing your work. Keeping files on the cloud (GitHub.com) makes your work error-proof because your files on GitHub.com are kept by a professional-grade system. After performing the above operations (`git add` and `git commit`) you can check the status of your repository, using `git status`. Below what git returned when I used the command `git status`:

```
(base) francopestilli@francos-mbp francopestilli % git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
(base) francopestilli@francos-mbp francopestilli %
```

As you can read from the message all is good. There is nothing to commit, I am working on a clean tree of the repository, but, git notifies us that `Your branch is ahead of 'origin/main' by 1 commit.` This means that my local copy of the repository is different (it is ahead of or it has a newer file version) than the one on the cloud, `origin`. So the next thing is to fix that. 

#### Pushing to origin to synch the local and cloud repositories

After changing a file and committing to its most recent version, the final step of the git/GitHub workflow is to push the local repository living on your machine to the cloud. To do so, we will use the command `git push`, this command will copy the local versions of your repository to the repository stored at https://github.com/yourUserName/yourUserName. The way I would do it is the following:

```
git push
```

To synch with GitHub.com, you *might* need to confirm your credentials. If you do not, please disregard this section and Skip to **6**:

```
(base) francopestilli@francos-mbp francopestilli % git push
Username for 'https://github.com': #######
Password for 'https://francopestilli@github.com': #######
```

Below is the output in the terminal with the results of the operation above. (If you are having problems with authenticating at this stage, please see Note 1 at the bottom of this tutorial. It explains how to create an access token to use instead of password-based authentication.)

```
(base) francopestilli@francos-mbp francopestilli % git push
Username for 'https://github.com': francopestilli
Password for 'https://francopestilli@github.com': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 563 bytes | 563.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/francopestilli/francopestilli
   0d544b9..c934e0d  main -> main
(base) francopestilli@francos-mbp francopestilli % 
```

### 6. Summary of everything above.

Okay! This tutorial was not short. It was definitely longer than the previous ones. After all this work this is what we have done:

  - Created a repository on GitHub.com.
  - Cloned the repository locally on your computer.
  - Made changes to a file inside the repository.
  - Added the changes to the stack of changes in the local git repository.
  - Committed the changes to the record of the local repository.
  - Pushed the local repository to GitHub.com

Now the local copy and the copy of the repository on GitHub.com are all in sync and your README.md file was updated. You can continue editing this file and use MarkDown to make it better and better.


_________________________________________________________________________________
###### Note 1. ##### Note 3. Configure git credentials (Optional if everything works for you with git)
To work with `git` on my computer we will need to be able to communicate between the cloud (GitHub.com) and your local computer. To do so, it is convenient to first perform some operations to set up your GitHub account on your computer and link your credentials on GitHub.com and your local file system. Indeed, we will need to be able to *shake hands* between files that live locally on your computer hard drive and copies of the same files stored on the computers used by GitHub.com (what I referred to above as "the cloud" or later on as `origin`).

After navigating to your git location we will set up some parameters git will use to notify GitHub about your user account on GitHub.com.  So, let's type the following commands in the terminal:

``` 
git config --global user.name "francopestilli"
git config --global user.email "pestilli@utexas.edu"
```

The `git config` command sets the basic configuration parameters of git and makes a record on your local computer. You will need to change my information and instead use your own GitHub ID and associated email address. These will save a record of the GitHub user ID and email. This operation will be performed once, and then GitHub will know who is sending files to the cloud.

The next configuration that it is helpful to do before starting with Git and the terminal is the text editor used by git on your local machine. The command we suggest to use on Mac OSX at the beginning is the following:

```
git config --global core.editor "/System/Applications/TextEdit.app"
```

On a Windows computer, you might try something like the following to set up `notepad` to read and write git log files and commit messages:

```
git config --global core.editor "c:/Windows/System32/notepad.exe"
```

There are many editors to choose from and data scientists "geek over" their editor. For example, I am currently using [Visual Studio Code](https://code.visualstudio.com/) a.k.a. `VS code`. `VS code` is a recently updated editor by Microsoft (note that we receive no money from Microsoft for this course). `VS code` is very slick and with nice features, especially for [the completion of blocks of code](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode). 

Git has many other configuration parameters. Yet, for a start, this will be all we need. If you are interested in exploring more of the other parameters, the following is a command that will display the list of parameters and their setting on your computer: 'git config --list', you can also learn more about `git config` by typing the following help command `git config -h`. In the future, you might need to set other configuration parameters but for this tutorial, we are done! 

###### Note 2. GitHub Access Tokens. 
In 2021, GitHub.com eliminated the option of allowing passwords for operations such as git push. Using a password was deemed not safe enough. In alternative, GitHub is suggested to use a personal access token. A personal access token is just like a password, but it is created automatically by GitHub, it does not necessarily apply to all operations on your account (a token can be limited to only a few operations) and it expires after a certain amount of time. [This is the article GitHub published explaining why they made this change and how to create an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). This is a short video that shows how to generate a GitHub Access token. Tokens should be treated just like passwords, kept in a secure location and never shared.

[![This is a short video that shows how to generate a GitHub Access token.](https://img.youtube.com/vi/WmDTEADPahg/0.jpg)](https://www.youtube.com/watch?v=WmDTEADPahg). 

###### Note 3. My preferred way to `git commit`. 
The above follows a standard workflow and shows how to commit changes to a file using a two-step process: `git add` and then `git commit`. In my normal workflow, I eliminate one step by using a single command that does both commits and adds: `git commit -am "This is my message"` the option `-a` in the previous command means `git add` so the commit command will do all at once a `commit` and an `add`. I find this a more convenient way to handle my workflow as this method eliminates one command, less typing is better than more typing!




