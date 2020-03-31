A collection of commands, tips, and tricks that you'll use all the time

#### Important!
Development tools are, by definition, dangerous if misused. NEVER RUN CODE FROM AN UNTRUSTED SOURCE.
We'll learn a bit more about what is trustworthy and what is not, but if you come across a script
and you want to use it... you better understand what it's doing before you do it.  Same goes
for snippets you put in the Terminal if they use commands that grab things from the internet,
like `curl`, `wget`, and lots more.

#### python2 vs python3
- sometimes you'll get lucky and `python my_python3_script.py` will work fine, but if you
ever see an error that seems strange the FIRST THING YOU SHOULD DO is check to make sure you
used the right python to run your script `python3 my_python3_script.py`

#### Git
Git is a way of sharing code amongst many people; everyone keeps a 'local'
copy of the code repository (AKA 'repo') on their computer in addition to
a 'remote' or 'origin' copy, which in our case is hosted by GitHub. So you
need to consider how your local copy is synchronized with the remote server's
version. A 'branch' represents a current state of the repo, and for most of
this class you'll all make local changes to a branch that I've given you, without ever 
pushing them to the remote.
- `git clone <name of a repository>` is a command you will likely run just
once; it sets up a local copy of a remote repository
- `git branch` view the current branches you have
- `git fetch` updates your local repo to KNOW ABOUT the latest changes in the remote, but 
doesn't apply them.
- `git pull` does a `git fetch` and then also merges any changes from the remote
version of the branch you're on into the local copy of the branch. We'll use this one
extensively 
- `git checkout <name of branch>` will switch to the branch you provided
- `git checkout -b <name of new branch>` will create a branch based off your
current branch with the name you provided
- `git branch -d <name of branch>` deletes a branch from your local repo; note that
you can't delete the branch you're on.

#### Terminal (AKA command prompt, command line, CLI, bash, shell)
- `pwd` will print out the 'present working directory', which is the folder
you are currently in
- `ls` lists the files and folders in your current location
- `ls -l` lists files/folders in current location with a bit more information
- `cd <the name of a folder>` will 'change directory' to that folder
- `cd ..` changes directory up one level, `cd ../..` changes directory up two levels, 
`cd ../../..` does 3 levels, etc.
- `cd` with nothing after it changes to your 'home' directory, `/home/<your user name>`
- `cd ~` is equivalent to `cd`; `~` is an alias for your home directory so no matter what 
your PWD is, you can do things like `python3 ~/my_script_in_home_folder.py`
- <Ctrl-z/x/c/v> don't work! Well actually they do, but they mean something
to Linux in the terminal (especially <Ctrl-c>, more on that later).
If you have a mouse with a scroll button, pressing it is equivalent to 
<Ctrl-v>, but otherwise you have to right-click and use the menu
