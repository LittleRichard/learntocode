A collection of commands, tips, and tricks that you'll use all the time


#### Ubuntu in a VM
- copy-paste across host and virtual machine should work

#### Git
Git is a way of sharing code amongst many people; everyone keeps a 'local'
copy of the code repository (AKA 'repo') on their computer in addition to
a 'remote' or 'origin' copy, which in our case is hosted by GitHub. So you
need to consider how your local copy is synchronized with the remote server's
version. A 'branch' represents a current state of the repo, and for most of
this class you'll all make local changes to a branch that I've given you
- `git branch` view the current branches you have
- `git fetch` updates your local repo to KNOW ABOUT the latest changes in the remote, but doesn't apply them.
- `git pull` does a fetch and then also merges any changes from the remote
version of the branch you're on into the local copy of the branch


#### Terminal (AKA command prompt, command line, CLI, bash, shell)
- `pwd` will print out the 'present working directory', which is the folder
you are currently in
- `ls` lists the files and folders in your current location
- `ls -l` lists files/folders in current location with a bit more information
- `cd <the name of a folder>` will 'change directory' to that folder
- `cd ..` changes directory up one level
- `cd ../..` changes directory up two levels
- `cd` with nothing after it changes to your 'home' directory, `/home/<your user name>`
- <Ctrl-z/x/c/v> don't work! Well actually they do, but they mean something
to Linux in the terminal (especially <Ctrl-c>, more on that later).
If you have a mouse with a scroll button, pressing it is equivalent to 
<Ctrl-v>, but otherwise you have to right-click and use the menu