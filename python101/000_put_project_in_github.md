Git is the most commonly used tool for 'source control', which aims to solve a few problems
- backing up all of your precious code
  - 'oh no i microwaved my hard drive! i spent so much time on that!'
- versioning and release consistency
  - 'wait which code is running on my server right now?'
- developer sanity during large projects
  - 'wait what happened, this was totally working 20 minutes ago; what did i change?'

For more details and commands, see in this project:
Set up your own project by creating it in github and then doing this, but with your project instead of this one: 
000_setup_to_use_git.md

Some commands for using git and a brief overview in a section of this how-to:
000_commands_cheatsheet.md

I won't bother re-writing guides on how to use git here, there are tons of them on the internet if you look for
'git for beginners'.  Hopefully some of those combines with the docs in this repo will get you far enough!

#### when should i use a branch?
Tough to say, it depends on how organized you want to be. This is a path to madness if it's just you working on
a project, but can also be useful for keeping large tasks separate. You'll feel this out as you go, but start without
branches until you get better at git.

#### when should i commit/push code?
Commit code any time you reach a milestone! For example, a few great milestone and corresponding commit messages would be
as follows. If you want to use branches to organize your work, these would also each be a great branch that you then
merge up to your master branch.
- 'added first script and requirements.txt file, confirmed libraries are installed in virtualenv.'
- 'pseudocoded the rough flow of the game, not actually doing anything yet'
- 'Handles user input to describe game parameters.  next up: use input to create game'
- 'creates game, but board display is buggy. committing anyway for sanity, debugging display next.'

Push code anytime you commit it!  It's not saved to the cloud until you push it to the remote repository! If you're collaborating
with other people you may choose a different approach, but that depends on how you're using your branches.

#### using github
Cruise over to the 'commits' tab inside a github project and review past commits.
If you're using branches, explore using pull requests to review code or share a proposed change with someone
