## First Push 
If it is your first time pushing up to GitHub, there is a little security hoop we have to jump through. We're going to create a super-secret password called a "token" and use that to login to GitHub from git. So, if after you do your first `git push`, if you are prompted for a password, please do the following:

### Gitting a GitHub token

* Go to your GitHub account
* Click your profile photo in the upper right
* Click "Settings"
* Click "Developer settings" in the left sidebar
* Click "Personal access tokens"
* Click "Generate new token"
* Check all the things
* Select "Expiration" and set to never/infinite
* Click "Generate token"
* Click the little copy button (two overlapping squares) 

### Entering the token

* Go back to the terminal
* Enter you GitHub username in the  "Your Name" prompt
* Paste your token into the password password prompt
* Hit <return>

### You're all set

This was a one-time thing. You shouldn't be prompted for a password again. In the future, if you wish delete this token and get more fancy with your security, you can delete this token by going back to Settings -> Developer settings -> Personal access tokens.
