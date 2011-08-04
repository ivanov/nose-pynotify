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
    n = pynotify.Notification(test.shortDescription(),
            "Error: " + str(err[0].__name__) +
            "\n" + str(err[1]), 'gtk-no')
    n.show()
    self.errors += 1

  def addFailure(self, test, err):
    """Called upon encountering a failure"""
    # Update counter
    n = pynotify.Notification(test.shortDescription(),
            "Failed: " + str(err[0].__name__) +
            "\n" + str(err[1]), 'gtk-no')
    n.show()
    self.failures += 1

  def begin(a):
    """Called before running any tests, used for initialization"""
    # Initialize pynotify
    pynotify.init(os.getcwd())

  def options(parser,env):
    """Called to allow plugin to register command line options with the parser."""
    # TODO: add option to of avoiding individual error/failure notifications
    pass

  def finalize(self, result):
    """Called upon the completion of all tests"""
    # Grab icon
    if self.failures > 0 or self.errors > 0:
      icon_name = "gtk-no"
    elif self.successes > 0:
      icon_name = "gtk-yes"
    else:
      icon_name = "dialog-question"

    # Generate and show the message at the end of the test
    n = pynotify.Notification(self.cwd,
                              self.msg % (self.successes,
                                          self.errors,
                                          self.failures),
                              icon_name)
    n.show()    
