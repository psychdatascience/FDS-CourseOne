## Tutorial 2: GitHub Overview and Account Creation

Author: Franco Pestilli, The University of Texas at Austin

Learning Goals:

* Create and account on GitHub 

Prerequisites:

* Internet access

### What is GitHub?

GitHub is a website (platform) containing an ensemble of software services for the management of code, data, and the collaboration of scientists and developers. 
This means that you can go to [GitHub](https://github.com) to access services (software running on cloud systems) that are meant to help you keep under control 
projects related to software, (small) data, text and figures. 

GitHub uses [git](https://git-scm.com/) to allow users to perform code [version control](https://en.wikipedia.org/wiki/Version_control). When developing software it is extremely helpfulp to keep under control each change (smaller or bigger) made to an existing code base. The process of keeping track of changes made to code is generally referred to as version control (also known as revision control, or code management). Version control is generally applied to a variety of classes of software systems such computer programs, documents, web sites, or other collections of information. Version control is a key component component of a Data Science project. Version control helps you keep up with what you are doing with your code and if you were to make a mistake (everyone makes mistakes, especially with software) version control can help you track back where the mistake was made and correct the mistake.

Mistakes in software development are referred to as 'bugs', this terminology is the heritage of the time when computers where not personal yet, but where shared and big and occupied entire rooms (read [Software Bug on Wikipedia](https://en.wikipedia.org/wiki/Software_bug)]. It is said the at these early times of computing insects could enter the computer rooms and interfere with the work of scientists by introducing in the execution of a computer program.  

GitHub can helps you track down the mistake you make and either revert the code to a version before the mistake was introduced or change the code so to eliminate the mistake (see [here](https://en.wikipedia.org/wiki/Version_control) for more details on version control).

#### GitHub Documentation

GitHub provides videos and written documentation to help 'on board' new users. The videos and documentation can hell beginners navigate a very complex tool and in most of the case they can answer many questions you might have as you learn GitHub. 

[Here is the GitHub Documentation page](https://docs.github.com/en) 

[This is a nice video from GitHub that provides an overview on the many things it is possible to do with GitHub](https://www.youtube.com/watch?v=noZnOSpcjYY).

Using GitHub is primarily free (you can find their pricing model [here](https://github.com/pricing)). Yet, some of helpful and more advanced features require a paid plan. Alternatively, users working for educational organizations (those that have an .edu email account), can request a free GitHub account with additional 
features or receive discounted rates.

Here are resources on how to get a GitHub Educational account if you are a:

* [Student](https://education.github.com/benefits?type=student)
* [Teacher](https://education.github.com/benefits?type=teacher)

Below is a video to get you started with creating a GitHub account using your .edu email. In the next tutorials, we will assume that you have already created an account, or do it together before moving to the next steps.

[![Example Video on How-To Sign Up on GitHub.com](https://img.youtube.com/vi/3m4pSljscEY/0.jpg)](https://www.youtube.com/watch?v=3m4pSljscEY)


#### Note about git. 

Git proposed a revolutionizing approach to software-version control. Git uses a distributed version control system. A dominant version control system preceeding git was Subversion (a.k.a., [SVN](https://subversion.apache.org/)). SVN is a centralized version control system. When using SVN a code repository is used by making a copy of the latest version of the repository. That copy is all a user has access to. This means that the entire repository (code and history of code changes) is only stored at the centralized location where the SVN repository was created and is managed. With git everyone who uses a repository and makes a local copy of a repository copies everything (i.e., code and code history). Whereas with a centralized system like SVN only the central-holder of the master-repository has a complete version of the code, with git any user has a complete copy of the repository (text for this note was adapted from [here](https://www.quora.com/What-does-it-mean-when-Git-says-distributed-is-the-new-centralized-and-local-branching-on-the-cheap-next-to-their-logo-on-the-website)).



