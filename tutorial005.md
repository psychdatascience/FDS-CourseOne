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

### First set using Git via a Terminal

To work with Git from your computer we will need to communicate between the cloud used by GitHub.com and your local computer. To do so, we will need to do some operations to set up your account and link your credential on GitHub.com and your local file system. Indeed, we will need to be able to shake hands between files that live locally on your computer hardrive and copies of the files stored on the computers used by GitHub.com (what I referred to above as "the could").

Open a terminal and navigate to the folder you have been using to handle git in the previous tutorials. Type the following in your terminal:

`
 cd ~
 cd git
`

The above steps are not necessary, but I tend to like to work with Git from the location where all my git files are. That is `/Users/francopestilli/git/' on my computer. This was explained in Tutorial 2 and 3. After navigating to your git location we will set up some paramters git will use to notify GitHub about your user acount on GitHub.com.  So, let type the following commands in the terminal:

` 
git config --global user.name "francopestilli"
git config --global user.email "pestilli@utexas.edu"
`

The `git config` command sets the basic configuration parameters of git and makes a recond on your local computer. You will need to change my information and instead use your own GitHub ID and associated email address. These will save a record of the GitHub user ID and email. This operation will be performed once, and then GitHub will know who is sending files to the cloud.

The next configuration that 


