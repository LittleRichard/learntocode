# Learn to Code!

This repository is a collection of scripts that are used to teach programming.  The
concepts should be broadly applicable, but we'll be learning Python since it's 
approachable, has lots of libraries you can import to do complicated things for you 
(more on this later), and is very well supported by the open source community.

## Set up your development environment
### Operating system
It's easiest to develop on a linux operating system, which isn't as scary as you might think!  
If you have a mac, you're all set because apple OS is actually based on linux.  
If you have windows, then the best way to get linux running is to use a virtual machine player,
this one works well:
https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html

Then download the Ubuntu operating system (you'll typically want the LTS version), 
you'll need the ISO to install Ubuntu into a new virtual machine:
- https://ubuntu.com/download/desktop

This guide to glue it all together looks close enough:
- https://theholmesoffice.com/installing-ubuntu-in-vmware-player-on-windows/

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
be installed on a linux OS (mac or Ubuntu, definitely not Windows), but just in case:
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
