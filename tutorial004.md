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
We will not attempt to cover the terminal exhaustively, instead, we will focus on the basics needed to get you started and help you use Git and GitHub.

## The Terminal
We are used to looking at and operate our personal computers using graphical user interfaces (GUIs). This means that we routinely open files or folders by first finding them using the "finder" (mac) or "browser" (Windows) graphical interface and then clicking on them. We perform a search using a search bar. We navigate the internet using a browesr such as Chrome, Firefox or Safari, we write documents using Google Docs or Microsoft Word. All these are examples of software that uses graphical user interfaces or GUIs. GUIs have revolutionized computers effectively making them accessable to anyone. Before GUIs, however, there was the `Terminal`.

##### Question: Do you know who started the personal computer revolution (name individuals or a company)? 

The terminal is the command line (text) interface to your computer file system and operative system. It is now referred to as interchangebly as the terminal, console, shell, or command line. They were called "terminals" because they were literally the end of the line - information from a centralized computer (a "main frame" - generally in another room or even another building) came out as far as the terminus or terminal, and no further. The earliest terminal was the ["teletypewriter" or "tty"](https://en.wikipedia.org/wiki/Teleprinter), literally a modified typewriter. 

![The Teletypewriter, a.k.a TTY](https://user-images.githubusercontent.com/2119795/151270216-53e6940c-48dd-48c6-899a-de7b395fc3b8.jpg)

[Image source Wikipedia](https://en.wikipedia.org/wiki/Teleprinter)

Later a one-piece keyboard and monitor combination called a "console" took its place but, of course, these were also called terminals. The "shell" is the software that allows you to interact with the computer's operating system using terminal/console. It is mainly used to run other programs by typing the name of the program plus any options at the "command line", the place where your typing appears ([read here for more information](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)).

Today's "terminal/console" is not an antique thing you plug into your computer, but rather just a window on your desktop that looks and acts like the terminals of yore. But why would we want to seemingly step back in time like this? Because, despite the ease of use of the GUI interface to your computer, the terminal is powerful and often provides faster and easier ways of doing things once you get a little good at using it. In fact, there are still certain things that you can do using the terminal that you cannot do using the GUI.

##### Question: Do you know who broght back the terminal in the era of the personal computers (name individuals or a company and at least a couple of answers might be correct)? 

Most of the following examples will use Mac OSX to demonstrate how to access the Terminal and use basic shell commands. This is just because I happen to have access to a Mac OSX. If you are using Linux (Ubuntu for example) [here is a nice tutorial](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview) on how to access and use the terminal. If you are using Windows, the terminal application is called the "console". If you are on Microsoft Windows 10 you might look into the [new Terminal](https://www.microsoft.com/en-us/p/windows-terminal/).

## Opening a terminal
In Mac OSX you can find the terminal using the search bar.

[![Example Video on How-To Find The Unix Terminal on Max PSX 10.5.x](https://img.youtube.com/vi/g-U1c2ojls8/0.jpg)](https://youtu.be/g-U1c2ojls8)

After that, I suggest you add the Terminal Icon to your Dock.
 
[![Here is an example on how to do it.](https://img.youtube.com/vi/cE5zXT2aP9Y/0.jpg)](https://youtu.be/cE5zXT2aP9Y)

In Windows, locate and run the "console".

## The Unix/Linux Filesystem

https://en.wikipedia.org/wiki/Unix_filesystem

The filesystem appears as one rooted tree of directories.[1] Instead of addressing separate volumes such as disk partitions, removable media, and network shares as separate trees (as done in DOS and Windows: each drive has a drive letter that denotes the root of its file system tree), such volumes can be mounted on a directory, causing the volume's file system tree to appear as that directory in the larger tree.[1] The root of the entire tree is denoted /.

In the original Bell Labs Unix, a two-disk setup was customary, where the first disk contained startup programs, while the second contained users' files and programs. This second disk was mounted at the empty directory named usr on the first disk, causing the two disks to appear as one filesystem, with the second disk’s contents viewable at /usr.

https://linuxfoundation.org/blog/classic-sysadmin-the-linux-filesystem-explained/

## Navigating the filesystem

By default Unix/Linux Terminals will show some basic information to help identify the user the opened the terminal and the system the terminal was opened on. This information can seem trivial on a PC because well we know who we are and on which computer we are running. Yet remmeber that terminals were intially used by multiple users on different shared mainframe computers.

In the video above you can see that my user name (`francopestilli`) and computer names (`francos-mbp`) are reported:

`Last login: Wed Oct 27 21:00:12 on ttys000`

`francopestilli@francos-mbp ~ %`

In addition to that, the data of last login  (`Last login: Wed Oct 27 21:00:12`) is reported. 

![Example of Bash Shell Terminal in Mac OSX (Big Sur early 2022)](https://user-images.githubusercontent.com/2119795/151271026-9926f136-9c4a-4f25-b748-3187cc8adce5.png)

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

#### Let's do something with the terminal

##### (1) Let's make a new folder

###### (1.1) Open a terminal. 

Type `cd ~` to navigate to your home directory (indicated by the symbol `~`).

###### (1.2) Let's take a look at the folders and files we have in the home directory. 

Type `ls -l` This will show all you files and folders. Some of which you might know you have others might be new to you.

The Image below shows all the visible files in the home directory of the computer I am using.
<img width="1643" alt="terminal_windows_OSX_LS" src="https://user-images.githubusercontent.com/2119795/151272012-d7a4ee97-4393-4773-9b09-8de2ecd86c78.png">

###### (1.3) Let's now create a folder.

Type `mkdir git` this command will create a folder `git` that will use later on to organize the repositories from GitHub.
      
###### (1.4) Navigate inside the folder `git`.

Type `cd git`, the command will change our current location from the home dir (`~`) to the directory we just created. You can check that by typing `pwd` (print working directory), the command will show you the path to the current (working) directory.
      
<img width="1643" alt="terminal_windows_OSX_PWD" src="https://user-images.githubusercontent.com/2119795/151272499-1a828b1f-3605-4a3d-85d6-38cdba176145.png">

###### (1.5) Create a file inside the folder `git`

 Type `touch readme.md` This will create an empty file inside the current directory, that at this point should be the directory `git`.
      
###### (1.6) Edit the file `readme.md` and use MarkDown to make it informative.
 
 Write a short title using the top heading so to explain what the goal of the folder `git` will be. For example, "Folder for all my GitHub repositories"
 In the second line, write the name, surname, email and GitHub user of the owner of this folder (you), using a smaller headings.
 In the rest of the text describe in plain words what you plan to use this folder for. Hoow you created the folder and the file (describe the commands that you typed in the termial to create the folder `git`, the file `readme.md` and describe how you learned to do this all (hint. Refer to this class and this tutorial).

Note that, opening the file might be different with different computer setup. On my Mac OSX I have the [Apple developer tools](https://developer.apple.com/) installed, so I can type in the terminal `open readme.md` and the file will be opened using Apple Xcode. Alternatively, you can use TextEdit using the graphic interface.

<img width="559" alt="Open_an_MD_file" src="https://user-images.githubusercontent.com/2119795/151277814-a105a53e-fdea-43b0-8743-66bc282a5ee2.png">


#### A couple of notes. 

###### Note one. The Terminal is programmable and that means customizable. 

All this can be customized because the terminal is programmable, the interface and display of information by default can be chanhed by changing specific configuration files. We will not go over that as it is not relevat for the current topic but here is a couple of good resources [one](https://www.maketecheasier.com/customize-mac-terminal/) and [another, more advanced, one](https://medium.com/@charlesdobson/how-to-customize-your-macos-terminal-7cce5823006e).

###### Note two. Commands have options.

In the previous video video I use additional parameters (a.k.a. options) to generate richer outputs from the commands or to automatically delete folder and the files insdie the folder. You can find out more about how to use a command in Unix/Linux and the available options for the command by typing the comman followed by -h for help, for example `rm -h`
