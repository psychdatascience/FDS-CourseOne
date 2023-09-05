## Learn About the Git Workflow that will be used by this class

Learning Goals:

 * Learn and practice with the `git` workflow used by this class
 * Create a repository on GitHub.com.
 * Clone the repository locally on your computer.
 * Copy a file into the new local repository
 * Add the changes to the stack of changes in the local git repository.
 * Commit the changes to the record of the local repository.
 * Push the local repository to GitHub.com


### 1. The Canvas->Git->GitHub->Canvas workflow we will use.

We will now go over the steps necessary to update, work with and report on the tutorials and exercises for the reminder of the semester.


### 2. The Canvas->Git->GitHub->Canvas workflow we will use.

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
 cd MyGitCode
```

The command that will allow the repository online to be copied locally on your computer while maintaining an invisible link to your online repository living on GitHub is `clone`:

```
git clone https://github.com/yourUserName/yourUserName 
```

The command will make a copy of the online repository on the current directory on your computer. So let's check this. You can show your current directory `pwd`. You can see all files and folders in your current using `ls -l`. We can navigate to the new repository folder `yourUserName` using `cd yourUserName`. 

[![This video shows how to clone a repository already existing on GitHub.com using terminal on Mac OSX.](https://img.youtube.com/vi/G931KZx4Rhc/0.jpg)](https://www.youtube.com/watch?v=G931KZx4Rhc).

### 4. Edit your repository.

We want 
