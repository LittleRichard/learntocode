A collection of commands, tips, and tricks that you'll use all the time

#### Important!
Development tools are, by definition, dangerous if misused. 
- NEVER RUN CODE FROM AN UNTRUSTED SOURCE.
We'll learn a bit more about what is trustworthy and what is not, but if you come across a script
and you want to use it... you better understand what it's doing before you do it.  Same goes
for snippets you put in the Terminal if they use commands that grab things from the internet,
like `curl`, `wget`, and lots more.


#### Your development environment
For now, you have 3 programs that you should have open when you write code.
- Text editor to modify code: *Sublime Text*
- Source control to stay updated: *Git-Cola* (just a user interface for `git`)
- Command line interface to execute scripts (and everything else): *Terminal*


#### The most common mistakes
- python2 vs python3: sometimes you'll get lucky and `python my_python3_script.py` will work fine, but if you
ever see an error that seems strange the FIRST THING YOU SHOULD DO is check to make sure you
used the right python to run your script
```
python3 my_python3_script.py
```
- If you're wondering why your code isn't working but you're 100% sure you wrote it correctly...
don't forget to save your script before you run it!!! <Ctrl-s> is the shortcut in sublime.


#### Code blocks and documentation notation
- a 'code block' is typically denoted with backticks, and 'markdown' files like this
one (as well as Wikipedia) will show them differently. `you can't see the backticks
surrounding this statement in a web browser because GitHub applies the code block style, 
try opening this file in a code editor instead!`.  You can also use triple backticks:
```
triple backticks denote a code
block with multiple lines, which you probably saw or
copy-pasted while installing development tools
```
- you'll see lots of comments like this in documentation and code `<name of a value>`,
this is intended to be interpreted without the `<>`, and a value as described by the name
inserted in its place; this almost always means a hard-coded value like `5.0` or `'abc'`,
or a variable name like `my_variable`.
For example:
```
# To use the print function in python, invoke it with the string you want printed:
print(<your string here>)  # note that this is not valid code (syntax), just documentation

# which you would then replace with something like:
print('hello world')
```

#### Terminal (AKA command prompt, command line, CLI, bash, shell)
- Terminal is your file/folder navigator as well as a way to order your computer to
execute commands and programs. *Get good at using the command line*, it's extremely 
useful and you'll use it a ton.
- Terminal will (mostly) expect you to enter arguments separated by spaces, so
do yourself a favor and NEVER USE FILE NAMES WITH SPACES. It's usable, but annoying.
- Tab-completion is your best friend! There's no need to type out the full names of
scripts, folders, or even programs! Type a few characters and hit tab to let the
terminal type it out the rest of the way.  Not working?  There are probably multiple
things with that name and you need to add more characters for your computer to be sure.
- If you ever issue a `sudo` command, this means that you are telling the computer
to execute the command after the word `sudo` as a Super User (AKA an admin). It will
prompt you for a password, which should be the same one you logged in with. It will
not 'echo' anything you type back to the screen, for security reasons, but never fear!
Just type your password and hit enter.
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
to Linux in the terminal (especially `<Ctrl-c>`, more on that later).
If you have a mouse with a scroll button, pressing it is equivalent to 
`<Ctrl-v>`, but otherwise you have to right-click and use the menu


#### Git
Git is a way of sharing code amongst many people; everyone keeps a 'local'
copy of the code repository (AKA 'repo') on their computer in addition to
a 'remote' or 'origin' copy, which in our case is hosted by GitHub. So you
need to consider how your local copy is synchronized with the remote server's
version. A 'branch' represents a current state of the repo, and for most of
this class you'll all make local changes to a branch that I've given you, without ever 
pushing them to the remote. We'll use a program with a user interface to do the work here,
but all it's really doing under the covers are these commands (plus a few others):
- git is a program that you can give commands to. Try `git help` to see them all. Some
of them are summarized in following bullet points.
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
