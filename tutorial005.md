## Using Git and GitHub via the terminal

Learning Goals:

* Set up GitHub on your computer
* clone a repository locally on your computer (using Unix/Linux Terminal commands)
* make changes to the repository (adding a file and editing a file)
* make a commit to record the changes
* push the changes upstream, i.e. to repository stored on the cloud on GitHub.com

Prerequisites:

* Internet access on linux or Unix based computer
* Git Installed
* A GitHub account and ability Create a GitHub Repo, i.e., ([Tutorial 2](https://github.com/psychdatascience/FDS-CourseOne/blob/main/tutorial002.md)) and [Tutorial 3](https://github.com/psychdatascience/FDS-CourseOne/blob/main/tutorial003.md)

### A reminder for version control.

In this tutorial we will learn how to perform some of the operations done with GitHub using the Web-UI but instead using the command line interface, the Linux/Unix terminal, on your local computer. To do so, we will need to have Git installed on your comouter. [Here is a guide to installing git.](https://github.com/git-guides/install-git). We will assume that that is the case and ask the others to find a way to install Git on their OS.

Just as a reminder. Version cotnrol is a system to keep track of files and folders for a computer file system. We all have used some sort of version control. For example, I like to save files on my computer with the following naming convention `year-collaborator-project-some_details.ext`, say `2022-larry-datascience-to_do_list.pdf`. I like to save files in folders also organized by date: `/Users/francopestilli/UTAustin/Teaching/2022/Spring/DataScience/`. I then update the same file or make new versions of the file every year. When I update files and folders I change the year in their name. Many of us have performed similar operations, manually, and many of us have encoutnered the challange of developing a good way to keep track of file names and being more or less diligent in updating the file names. A version control system is a way to use computers to do what humans are not very good at: Keeping track of small changes, updating files as their are modified, rembering to update records.

### Set up Git via the Terminal

To work with Git from your computer we will need to communicate between the cloud used by GitHub.com and your local computer. To do so, we will need to do some operations to set up your account and link your credential on GitHub.com and your local file system. Indeed, we will need to be able to shake hands between files that live locally on your computer hardrive and copies of the files stored on the computers used by GitHub.com (what I referred to above as "the could").

Open a terminal and navigate to the folder you have been using to handle git in the previous tutorials. Type the following in your terminal:

```
 cd ~
 cd git
```

The above steps are not necessary, but I tend to like to work with Git from the location where all my git files are. That is `/Users/francopestilli/git/' on my computer. This was explained in Tutorial 2 and 3. After navigating to your git location we will set up some paramters git will use to notify GitHub about your user acount on GitHub.com.  So, let type the following commands in the terminal:

``` 
git config --global user.name "francopestilli"
git config --global user.email "pestilli@utexas.edu"
```

The `git config` command sets the basic configuration parameters of git and makes a recond on your local computer. You will need to change my information and instead use your own GitHub ID and associated email address. These will save a record of the GitHub user ID and email. This operation will be performed once, and then GitHub will know who is sending files to the cloud.

The next configuration that it is helpful to do before starting with Git and the terminal is the text editor used by git on your local machine. The command we suggest to use on Mac OSX at the beginning is the following:

```
git config --global /System/Applications/TextEdit.app
```

On a Windows computer you might try something like the following to set up the `notepad` to read and write git log files and commit messages:

```
git config --global core.editor "c:/Windows/System32/notepad.exe"
```

There are many editors to choose from and geek data scientists "geek over" their editor. For examlple, I am currently using [Visual Studio Code](https://code.visualstudio.com/) a.k.a. `VS code`. `VS code` is a recently updated editor by Microsfot (note that we receive no money from Microsofot for this course). `VS code` is very slick and with nice features, especially for [the completion of blocks of code](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode). 

Git has many other configuration parameters. Yet, for a start this will be all we need. If you are interested in exploring more the other paramenters, the following is a command that will display the list of paramters and their setting on your computer: 'git config --list', you can also learn more about `git config` by typing the following help command `git config -h`. In the future you might need to set other configuration parameters and set 

### Create a new repository and start editing it

We will now create a new repository, and edit files and directories in it, perform commits via the Terminal. To preactice we will create your own GitHub Resume. GitHub recently allowed users to create a repository that can be used as landing page for your GitHub page. A sort of CV that will display as people navigate to your GitHub account. Data science geeks will like the idea of having a slick set up and appealing GitHub page as that page is your passport to the world of data science!

So, first let repeat some of the steps of Tutorial 3 and create a repository on GitHub.com:

#### Navigate to GitHub.com/yourUserID and Sign in to your account.

First, navigate to GitHub.com and *sign in*. 

[![This is a Video Reminder on How to Login on GitHub, if neeed](https://img.youtube.com/vi/KGLG-0VIEDM/0.jpg)](https://www.youtube.com/watch?v=KGLG-0VIEDM)

#### Create a repository: Using the Web User Interface (Web UI).

Next create a new repository. Importantly, the name of the repository should *match* your GitHub user ID (in my case the repository will be named `francopestilli` because that is my user ID on github, see here: https://github.com/francopestilli 

[![This is a video showing how to create a new repository using the graphical interface on GitHub. The name of the repository is special as it matches the user's ID.](https://img.youtube.com/vi/qijRlJpBm9A/0.jpg)](https://www.youtube.com/watch?v=qijRlJpBm9A).

After all this, if you navigate to your GitHub Resume Repository: https://github.com/yourUserName/yourUserName (change the URL to use your real user name), you will see something like the following:

<img width="1393" alt="YourGitHubResumeRepo" src="https://user-images.githubusercontent.com/2119795/151894081-ecb31b0e-9556-4911-a37d-5326db550f0b.png">

#### Clone the new repository from GitHub.com onto your local computer.

Next on your local computer, navigate to the root of your `git` repositories:

```
 cd ~
 cd git
```

The command that will allow the repository online to be copied locally on your computer whil emaintaining an invisible link to your online repository living on gitHub is `clone`:

```
git clone https://github.com/yourUserName/yourUserName 
```

The command will make a copy of the online repository on the current directory on your computer. So let's check this. You can show your current directory `pwd`, we just navigated to it a few lines above, if all went well it should be `git`. You can then list the files and folders in the repository using `ls -l`. You should see a folder named `yourUserName`. 


[![This video shows how to clone a repository already existing on GitHub.com using terminal on Mac OSX.](https://img.youtube.com/vi/G931KZx4Rhc/0.jpg)](https://www.youtube.com/watch?v=G931KZx4Rhc).

#### Start Editing your repository using the terminal.

Next, we will edit the readme.md file that came with the repository. While doing this, we will temporarily put the terminal aside (do not close it, just minimize the window). We will then use any editor to edit the readme.md file that came with the repository we just cloned. This is just like what we did in [Tutorial 003](https://github.com/psychdatascience/FDS-CourseOne/blob/main/tutorial003.md#4-edit-a-repository-edit-an-existing-file). Pick your editor of choice, edit the readme.md fie and let's add your First Name, Middle initials and Family name as Title header, after that let's add a tag-line that can give a quick sense of who you are for example *I am a professor at The University of Texas at Austin interested in Psychology, Neuroscience and Data Science.* After that let's write a short biography. Write something short about your background, for example I would write: *I am from Rome and I am here because I believe in science and education and I would like to think that by teaching young minds how to think critically and cutting edge tools, like coding, we can make the world a better place. It is not simple, but I believe we can.* Finally, finish editing, save and close your editor. Now we are ready to make our first commit. 

First let's learn how to take a look at the status of your local repository. Let's go back to the terminal and type:

```
git status
```
Below what the command returns for me after I edited the README.md:

```
(base) francopestilli@francos-mbp francopestilli % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   README.md
```

As you can see git has detected changes to the `README.md` file. 




