### File I/O tutorial

#### Make a new repo and clone it to your computer
For this tutorial, make a new GitHub repo. Name it "PythonTutorials" or "FDSPython" or whatever you want. Then clone the repo onto your local machine (for example you can copy it inside: `/Users/YourUserNameOnYourPC/GitHub/PythonTutorials or /Users/YourUserNameOnYourPC/git/PythonTutorials`). You'll now have a folder with the same name in your local GitHub directory. 

#### Make a datasets subfolder
Inside this folder, make another folder (you can use the command `mkdir` to do so) named "datasets". If you named the first folder "PythonTutorials", you should now have a

``.../GitHub/PythonTutorials`` folder and a

``.../GitHub/PythonTutorials/datasets`` folder 

(or similar – the important thing is that your "datasets" folder is a subfolder of wherever you are going to keep your Jupyter notebooks)

##### Note: 
Don't use black spaces in your file or folder names for Python, MatLab, the Terminal or when using R. Even though your computer's operating system graphical interface allows using spaces in your file/folder names, the black-spaces wreaks havoc when you try to read and write files from your own programs.

#### Download the tutorial files
Once you have have a folder, download the Tutorial 006 .ipynb file from Canvas and the Data File for Tutorial 006 .csv file also provided on Canvas. Move then the .ipynb notebook into the first folder (`.../GitHub/PythonTutorials`), and the .csv file into the second (`.../GitHub/PythonTutorials/datasets`). 

#### Git Commit Push your modified local repo up to the cloud
To do this you can do somehting like the following:

A) `git add /Users/YourUserNameOnYourPC/GitHub/PythonTutorials/`

B) `git commit -am "Your nice commit message here"`

C) `git push`. 

Now you can push your repo up to GitHub so it's all nice and backed up on the Cloud!

#### Begin the tutorial!
Finally, fire up the jupyter notebook from your terminal (or launch it via Anaconda), open the tutorial, and have at it!

To do this, in a terminal window you can do something like the following:

`jupyter notebook`

This last command will open your web browser and a file-browser in it. You should be able to see the jupyter notebook for tutorial 006. Open that, it will appear in a new web-browser window. You will be now ready to run the code in `tutorial006.ipynb`.
