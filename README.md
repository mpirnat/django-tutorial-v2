django-tutorial-v2
==================

This repository contains the code for version 2 of the
"Web Development with Python and Django" tutorial session run by
[Mike Pirnat][mpirnat] and [David Stanek][dstanek].

In this tutorial we'll build a website step by step
using the [Django][django] web framework.


Getting Started
---------------

If you're attending the tutorial in person,
**please** make sure you install these prerequisites
**before the class begins**
so that we can make the most of our time together.
You and your fellow attendees will
thank you for your preparedness!

You'll need to install:

 1. [Python 3.4][python]

  Django is written in the Python programming language;
  you'll need to install Python
  in order to make anything work.

  You should install **Python 3.4**.

  Earlier versions of Python are not guaranteed
  to be compatible with the example code
  in this repository.

 2. [Git][git]

  You will need the Git version control system
  in order to work with the exercises in this repository.
  If you're new to Git, don't panic!
  We won't be doing anything too weird,
  and we'll walk through all of it
  during the session.


Setting Your Path (Windows)
---------------------------

**If you're on Windows**,
you may need to update your PATH
so that Window can find your python.exe.
This varies a bit between
[different versions of Windows][windows-path]
so use the method that's right for your OS.

Since you installed Python 3.4, add:

    C:\Python34\;C:\Python34\Scripts\;C:\Python34\Tools\Scripts


Setting up the Project
----------------------

Once you have installed these basics,
let's get the working environment set up for the project.
Time to open up a command line!
(Terminal in Mac OS X,
good ol' "cmd" in Windows.)

 1. Create a new virtual environment ("virtualenv") and activate it

  On Linux or Mac OS X:

      $ pyvenv django-tutorial-v2
      $ cd django-tutorial-v2
      $ source bin/activate

  On Windows:

      > pyvenv.py django-tutorial-v2
      > cd django-tutorial-v2
      > Scripts/activate.bat

 2. Clone this repository

  In the django-tutorial-v2 directory from the previous step:

      $ git clone https://github.com/mpirnat/django-tutorial-v2.git ./src

 3. Install Django and any other Python dependencies

  In the django-tutorial-v2 directory from the previous step:

      $ cd src
      $ pip install -r requirements.txt

  Or, on Windows:

      > cd src
      > pip.exe install -r requirements.txt

 4. Check to make sure everything's in good shape

  In the src directory from the previous step:

      $ python prerequisites.py

  On Windows, that looks like:

      > python.exe prerequisites.py

 5. Rewind the repository to the start of our exercises

  In the src directory from the previous step:

      $ git reset --hard exercise01.1

You should now be ready for the tutorial!


Slides
------

The current slides that accompany this tutorial are
[available for viewing and downloading][slides].


Help!
-----

If you need help getting set up, please contact
Mike Pirnat (mpirnat@gmail.com) and
David Stanek (dstanek@dstanek.com).
Please make sure to copy both of us
so that we can make sure you get the best answer as soon as possible.


Other Versions
--------------

Looking for an earlier version of this tutorial
as presented at CodeMash 2013 and 2014?

It's [available from the original GitHub repository][v1].


Credits
-------

This tutorial was created by:

 * [Mike Pirnat][mpirnat]
 * [David Stanek][dstanek]

Based on the tutorial originally created with [Mike Crute][mcrute].

With gratitude to the Python and Django communities for their accomplishments.


[django]: https://www.djangoproject.com
[dstanek]: http://traceback.org
[git]: http://git-scm.com
[mcrute]: http://mike.crute.org
[mpirnat]: http://mike.pirnat.com
[python]: http://python.org/download/
[slides]: #TODO
[v1]: https://github.com/mpirnat/django-tutorial
[windows-path]: http://www.java.com/en/download/help/path.xml
