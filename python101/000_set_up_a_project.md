This will cover a common approach to setting up a python project and installing/using a few 3rd party libraries. 
There isn't going to be much python in this how-to, pretty much all of it will be commands in the terminal.

#### installing packages with pip
`pip` is an executable program (just like `python3`) that knows how to download and install python packages that
other people have published.  This is how you would set up a library/package you want to use; first you 
`pip install <name of package>`, and then from python scripts you can `import <name of package>`.

But this is a bit limited, because then you have to remember all of the packages you've installed... so let's
use a requirements file.  `touch requirements.txt`, and then put all the packages you want to use in there, like:
```
cmd2
flask
numpy
```
Then install the latest version of all of them at once by giving the requirements file to `pip`
`pip install -r requirements.txt`

Note: packaging and installation is a deep well with lots of 'more correct' ways to use it, but this is fine until
you need to install your app in the cloud somewhere.

#### don't just install stuff carelessly
First let's consider what happens if we don't put any effort into setting up a place for the project to live. 
- I use `pip` (more on this later) to install a library for a project on my computer and import it in my scripts
- I finish the project a year later, but can't use the latest version of that library because <this can happen for various reasons>
- I start another project, and want to use that library again.

Now I'm stuck, because I can't use the latest version in my new project without breaking the other project.  If only there was
a way to set up a sandbox unique to my project...
  
#### Virtual Environments
A virtual enviroment is exactly what we're looking for!  You can create as many of these as you need to (typically one per project),
and as long as you switch your context into the right virtual environment before you install and run your code there's no difference.
- YOU MUST REMEMBER TO ACTIVATE YOUR VIRTUALENV FIRST!

Let's set one up for an arbitrary project called `my_proj`.  In the terminal:
```
# make a directory right here to hold the project
mkdir my_proj

# `python3`: chooses which version of python; you could install/use a specific python version like `python3.8` if that's what you want
# `-m venv`: tells python you're creating a virtualenv
# `my_proj`: a path to a folder where the virtualenv should be created, for example: `my_projects/python/my_proj`
# Note: you may need to `apt-get` a couple more things, but try it and see what it tells you
python3 -m venv my_proj
# if you needed to `apt-get`, your virtual env may be in a weird state.  delete it and try again
rm -fr my_proj
python3 -m venv my_proj

# cd into that directory and you should see a few things created by virtualenv setup, notably the `bin` folder
cd my_proj
ls -l

# to activate your virtual environment, do the following; you must do this EVERY TIME YOU OPEN A NEW TERMINAL
# and plan to run this project
source bin/activate
```

#### source bin/activate
Bits & Bytes here... the key thing to know is that once you've activated your virtualenv, it re-directs any usage
of `python` and `pip` to be the `python`/`pip` that is associated with the virtualenv (instead of the system default).
By using the `pip` in the virtualenv, all installed python packages will automatically be scoped inside the virtual env.
Try it and see
```
# activate the virtualenv
source bin/activate 

# install cmd2, a python package
pip install cmd2

# open a command line python by passing no arguments
python3

# import your package
# >>> import cmd2  # this should work!
# >>> exit()  # exit the python command line

# deactivate your virtualenv
deactivate

# do the same thing again
python3
# >>> import cmd2  # BOOOOM, because cmd2 isn't installed outside your virtualenv
```

#### project setup checklist
- created a virtualenv
- created a requirements.txt file
- put all of the code inside the 

