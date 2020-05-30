This will cover a common approach to setting up a python project and installing/using a few 3rd party libraries.  First let's 
consider what happens if we don't put any effort into setting up a place for the project to live. 
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
python3 -m venv my_proj

# cd into that directory and you should see
```
