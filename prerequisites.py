#!/usr/bin/env python

import sys


# Check that we are in an activated virtual environment
try:
    import os
    virtual_env = os.environ['VIRTUAL_ENV']
except KeyError:
    print("It doesn't look like you are in an activated virtual environment.")
    print("Did you make one?")
    print("Did you activate it?")
    sys.exit(1)


# Check that we have installed Django
try:
    import django
except ImportError:
    print("It doesn't look like Django is installed.")
    print("Are you in an activated virtual environment?")
    print("Did you pip install from requirements.txt?")
    sys.exit(1)


# Check that we have the expected version of Django
expected_version = '1.7.1'
installed_version = django.get_version()
try:
    assert installed_version == expected_version
except AssertionError:
    print("It doesn't look like you have the expected version "
            "of Django installed.")
    print("You have {0}.".format(installed_version))
    sys.exit(1)


# All good, have fun!
print("Everything looks okay to me... Have fun!")
