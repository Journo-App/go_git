print "Go Git Instructions
This is going to be one very long string. 
If you already have a local directory made:
I created a directory (on my harddrive) called go_git then with Sublime Text created this file, go_git.py, which you are reading now.
On the command line I navigated to the go_git dir and typed: git init. 
This is a new directory that Git creates where all of the history for the project will be stored. The existance of a .git directory is also used to inform Git that we are working within a repository. The dot at the start of the directory name indicates that it is a hidden directory (you won't see it if you open the folder in through a graphical interface).
Next type git status. On the command line you should see: 

git status
On branch master
Initial commit
Untracked files:
(use "git add <file>..." to include in what will be committed)

go_git.yp
#
nothing added to commit but untracked files present (use "git add" to track)

This tells us  we are working on the master branch.

Here is a helpful tip from Thinkful: 

The next important piece of information Git gives when you type 'git status' is the status of the files. Currently you have two "untracked" files. These are files which are inside the repository but are not under version control. To take a step back, when you save a Word document, you only need to do one thing: hit "save." In Git, saving a file requires two steps: telling Git to track the file (what's called, "adding" it), and then saving it (what's called "committing").

Generally you don't want to have untracked files within your repository. So let's use git add to tell Git to track any changes we make to the files. Type the following line:

$ git add .

Then type git status. You should see something like this: 

$ git status
On branch master
Initial commit

Changes to be committed:
(use "git rm --cached <file>..." to unstage)

new file:   go_git.py 
(call the file whatever you want)

Next, commit the changes using the git commit command:

$ git commit -m "Initial commit"
The -m option here is used to give a description of what changes you made in the commit. The two files have now been committed succesfully. To confirm that everything was committed properly, type git status:

$ git status
On branch master
nothing to commit, working directory clean

When you see 'nothing to commit, working directory clean' == all your recent work was committed.

 Now send go_git (or whatever your dir is called) to GitHub. Go to the create new repository page in GitHub, fill in the information for your repository, and hit Create Repository.

Next copy the FIRST line of code you see in the second set of instructions

You already have a repo set up on the computer (remember, we created the go_git repo with the git init command). Toggle to the command line and paste the code you copied from GitHub:  

git remote add origin https://github.com/Journo-App/go_git.git 
(Journo-App is the name of my GitHub account. Yours != same and you can call your dir/repo something other than go_git)

From Thinkful: Here we are creating a remote called origin. This is the name which is conventionally given to your main remote. You should push changes up to your origin remote on a regular basis so you have an up-to-date backup of your code and its history.

Now, send your changes to the remote repository using the git push command
Type on the command line: git push origin master
You may be prompted to supply your GitHub account name (i.e. Journo-App in my case) and your pw. You can't tell that you're typing at this stage for some reason but just type it out and hit return. If you make a mistake you'll get a prompt. If you enter it correctly you see something like: 

Counting objects: 3, done.
Writing objects: 100% (3/3), 236 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Journo-App/go_git.git
 * [new branch]      master -> master

Toggle to GitHub and your repository should be listed there. I have a file in mine called go_git.py
Now you have to pull from a remote repository so that your version matches the version on a remote server. 
Type on the command line: 
git pull origin master 

and you should see: 

git pull origin master
From https://github.com/Journo-App/go_git 
 * branch            master     -> FETCH_HEAD
Already up-to-date.
 
(remember Journo-App will == your account and go_git will be whatever name you chose)


"