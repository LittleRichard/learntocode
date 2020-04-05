First we're going to 'clone' the remote repository to a local copy on your computer. Open a Terminal:
- Navigate to the folder you want to put the code in (see command line part of cheatsheet)
- Clone the repo from the remote server to a local copy
```
git clone https://github.com/LittleRichard/learntocode.git
```

This made a folder called `learntocode` in the folder you were in when you ran the `git clone`;
your local copy of the git repo lives in there so let's 'change directory' to it:
```
cd learntocode
```

For this edition of the class we're going to use a specific branch in our git repository, 
named `learntocode_lockdown`, so you should `checkout` that branch:
```
git checkout learntocode_lockdown
```

As we proceed through the classes, I'll `git commit` and `git push` more code to the
remote version of the branch, and you will download it to your local copy of the branch
with `git pull`.  Try that now, there shouldn't be any changes since you effectively
did a `git pull` when you cloned the repo.

You should also install a graphical interface for git, Git Cola seems reasonable:
- Ubuntu: 
```
sudo apt-get install git-cola
```
- Mac: 
```
brew install sphinx-doc
brew install git-cola`
```
