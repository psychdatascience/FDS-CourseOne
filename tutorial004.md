# Introduction to the Unix/Linux Terminal

Learning Goals:

* Learn about the Unix/Linux Terminal (or Windows terminal/console)
* Navigate the file system using the terminal
* Create a folders and a files with the terminal

Prerequisites:

* Internet access
* A computer with a terminal application. Basically, any computer (even a Chromebook!)

### Reading overview
This short reading is a very simple introduction to your computer's terminal. 
We will not attempt to cover the basics of the terminal exstensively, instead, we will focus on what is needed to master Git and GitHub.

## The Terminal
We are used to looking at and operate our personal computers using graphical user interfaces (GUI). This means that we routinely open files or folders by first searching them using the "file finder" graphical interface to find a folder or a file. We perform a serach using a search bar. We navigate the internet using a browesr such as Chrome or Safari, we write documents using Google Docs or Microsoft Word. All these examples use graphical user interfaces or GUI. GUI have revolutionized computers effectively making it personal, hence PCs or Personal Computers. Before personal computers and GUI there was text and the terminal.

###### Question: Do you know who started the personal comptuer revolution (name individuals or a company)? 

The terminal is the command line (text) interface to your computer file system and operative system. It is referred to as interchangebly as the terminal, console, shell or command line. They were called "terminals" because they were literally the end of the line - information from the computer came out as far as the terminus or terminal, and no further. Technically, the "terminal" was the software that printed text and allowed you to input text, the "console" was the hardware – literally a modified typewriter at first, and later a one-piece keyboard and monitor combination – and the "shell" was the software that sent the text to the terminal and interpreted the commands typed at the terminal for the operating system (the software that ultimately controls the computer).

The term `terminal` comes from the old days when computer systems were basically architected as today's supercomptuing systems ([read here for more information](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)). A centralized computer (main frame) was accessible by individual users only via terminals and command line interfaces. The centralized computer had the ability to compute but the terminals were only interfaces that allowed access to the storage and computing power using only a keyboard and a small screen.  
The terminal allowed only text to be transferred to the main frame computer. Technically, text consisted of basic commands for software called the "shell", which in turn manipulated the  programmable operative system. Linux (Ubuntu is one of the most diffused Linux distributions) is a programmable operative system. Mac OSX is also a programmable operative system. These system provide terminal access to files, directories (a.k.a "folders"), the ability to run simple programs to do things like copy a bunch of files at once.

Most of the following examples will use Mac OSX to demonstrate how to access the Terminal and use basic shell commands. This is just because I happen to have access to a Mac OSX. If you are using Linux (Ubuntu for example) [here is a nice tutorial](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) on how to access and use the terminal. If you are on Microsoft Windows 10 you might look into the [new Terminal](https://www.microsoft.com/en-us/p/windows-terminal/).

## Opening a terminal
In Mac OSX you can find the terminal using the search bar.

[![Example Video on How-To Find The Unix Terminal on Max PSX 10.5.x](https://img.youtube.com/vi/g-U1c2ojls8/0.jpg)](https://youtu.be/g-U1c2ojls8)

After that, I suggest you add the Terminal Icon to your Dock
 
[![Here is an example on how to do it.](https://img.youtube.com/vi/cE5zXT2aP9Y/0.jpg)](https://youtu.be/cE5zXT2aP9Y)

## Navigating the file system

By default Unix/Linux Terminals will show some basic information to help identify the user the opened the terminal and the system the terminal was opened on. This information can seem trivial on a PC because well we know who we are and on which computer we are running. Yet remmeber that terminals were intially used by multiple users on different shared mainframe computers.

In the videso above you can see that my user name (`frncopestilli`) and computer names (`francos-mbp`) are reported:

`Last login: Wed Oct 27 21:00:12 on ttys000`

`francopestilli@francos-mbp ~ %`

In addition to that, the data of last login  (`Last login: Wed Oct 27 21:00:12`) is reported. 

#### Useful commands that can be used in the terminal

We can type commands inside the Terminal that will allow us to perform operations on files and folders in the hard drive of the computer. There are many many commands in a Unix/Linux shell, see [here for a few](https://haydenjames.io/90-linux-commands-frequently-used-by-linux-sysadmins/).

In a terminal type:
`pwd` - a.k.a. `P`rint `W`orking `D`irectory. The command will show you the current location on your file system. This is the folder where your terminal would read or write files when requested. 

`ls` - a.k.a. LiSt. The command will show "list" the files and directories in your current directory.

`cd` - a.k.a. Change Directory. The command will allow navigating away from the current directory. For example `cd ..` will move up one directory, or `cd ~` will return to you home directory (the home directory is the one where the terminal generally start when first opeend.

`touch` - a.k.a. Touch a file to create the file. This command will create an empty file with the specified file lane for example: `touch franco.md` will create a file in the current directory with my name and the suffix `.md`.

`mkdir` - a.k.a. Make a Directory. The command will create an empty directory at the specified path, for example: `mkdir ~/franco_dir` will create an empty directory called `francos_dir` in the `home` directory.

`mv` - a.k.a. Move a file. This command will move files (and with advanced options also entire directories).

`rm` - a.k.a. ReMove a file or a directory. This command will delete files and directories (to remove entire directories additional parameters, the video below shows an example on ho wto delete a full folder).

Well these are the basic commands that we will need to use initially to use GitHub locally on our machines using the Linux/Unix terminal. We will learn a few more of them as we move forward with the readings.

Below a short Video that uses the commands above to give you a sense of the outputs. 

[![Using basic commands in the terminal](https://img.youtube.com/vi/zQsChRhwD5Y/0.jpg)](https://youtu.be/zQsChRhwD5Y)

#### A couple of notes. 
Note one. The Terminal is programmable and that means customizable. 

All this can be customized because the terminal is programmable, the interface and display of information by default can be chanhed by changing specific configuration files. We will not go over that as it is not relevat for the current topic but here is a couple of good resources [one](https://www.maketecheasier.com/customize-mac-terminal/) and [another, more advanced, one](https://medium.com/@charlesdobson/how-to-customize-your-macos-terminal-7cce5823006e).

Note two. Commands have options.

In the previous video video I use additional parameters (a.k.a. options) to generate richer outputs from the commands or to automatically delete folder and the files insdie the folder. You can find out more about how to use a command in Unix/Linux and the available options for the command by typing the comman followed by -h for help, for example `rm -h`
