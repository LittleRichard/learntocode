First we're going to 'clone' the remote repository to a local copy on your computer. Open a Terminal:
- Navigate to the folder you want to put the code in. You can use your home folder: `cd ~`
- Clone the repo, which is public so you don't need to authenticate: 
`git clone https://github.com/LittleRichard/learntocode.git`

For this edition of the class we're going to use a specific branch in our git repository, 
named `learntocode_lockdown`, so you should `checkout` that branch:
`git checkout learntocode_lockdown`

And then just to make sure you're up to date (which you should be if you JUST cloned it), we'll do 
a `pull`; this will update your local repo to know about any changes that occurred in the remote repo,
and then merge any remote changes to your branch into your local repo.
`git pull`

You should also install a graphical interface for git, Git Cola seems reasonable:
- Ubuntu: `sudo apt-get install git-cola`
- Mac: `brew install sphinx-doc`, then `brew install git-cola`
