"""
This module implements a pynotify-based notification system for nose tests.
Please see README.md for licensing info, an installation guide, and usage.
"""

import pynotify
import os
import sys

from nose.plugins import Plugin

class PyNotify(Plugin):
  """Subclass of nose.plugins.Plugin that displays a notification at the end
  of test suites, whenever enabled."""

  enabled = False
  name = "pynotify"
  score = 2

  def __init__(self):
    """Constructor"""
    # Run parent class' constructor
    super(PyNotify, self).__init__()

    # Set up number of successes, failures, and errors
    self.successes = 0
    self.failures = 0
    self.errors = 0

    # Generate msg title and body
    self.cwd = os.getcwd()
    self.msg = "%s successes, %s errors, %s failures"

  def addSuccess(self, test):
    """Called upon encountering a success"""
    # Update counter
    self.successes += 1

  def addError(self, test, err):
    """Called upon encountering an error"""
    # Update counter
    self.errors += 1

  def addFailure(self, test, err):
    """Called upon encountering a failure"""
    # Update counter
    self.failures += 1

  def begin(a):
    """Called before running any tests, used for initialization"""
    # Initialize pynotify
    pynotify.init(os.getcwd())

  def finalize(self, result):
    """Called upon the completion of all tests"""
    # Generate and show the message at the end of the test
    n = pynotify.Notification(self.cwd, self.msg % (self.successes,
                                                    self.errors,
                                                    self.failures))
    n.show()    
