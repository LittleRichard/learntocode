# Learn to Code!

This repository is a collection of scripts that are used to teach programming.

## Set up your development environment
### Operating system
It's easiest to develop on a linux operating system, which isn't as scary as you might think!  
If you have a mac, you're all set because apple OS is actually based on linux.  If you 
have windows, then the best way to get linux running is to use a virtual machine.  You can 
follow this guide to set up with an OS called Ubuntu:
https://itsfoss.com/install-linux-in-virtualbox/

### Code editor
There are a range of tools that you can use to edit code, which can be very simple 
(notepad) or very complicated (PyCharm).  We're going to split the difference 
and use Sublime:
https://www.sublimetext.com/3

Sublime is nice because it will do 'syntax highlighting', which turns parts of your code 
into colors that make it easier to read.

### Source Control
This website uses an open-source software tool called 'git', which is used by just
about any modern software company to manage versions of code.  It should already
be installed on your computer, but just in case:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

In our case, we'll use it to access scripts for lessons, as well as homework and 
solutions.  We'll cover some fundamentals of git, including getting set up to 
access this code repository, in the first class.

### Test if it worked
Open the program called 'Terminal' in Mac OS or Ubuntu-in-VM-on-Windows, type
`python3 --version`, and hit enter.  You have invoked the `python3` 
executable program with the `--version` option, which makes it print out 
the version and then exit.

You should see something like this, and if it's `3.6.<some integer>`
or `3.7.<some integer>` then you're all set.  If not, we may need to do a little more.
```
$ python3 --version
Python 3.7.1
```
