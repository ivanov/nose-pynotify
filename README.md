nose-pynotify
=============
<center><img src="http://colinfdrake.com/images/nose.png" /></center>

Implements a pynotify-based notification system for nose tests.

Installation
------------
To install nose-pynotify, use easy_install or pip:

    $ easy_install nose-pynotify
    # or
    $ pip install nose-pynotify

Or you can get it from the PyPI page/github repo and install it manually with setuptools:

    $ sudo python setup.py install

Usage
-----
To enable nose-pynotify for a single run, you can simply pass in a command-line switch:

    $ nosetests ... --with-pynotify

Or export the environment variable `$NOSE_WITH_PYNOTIFY` to enable the plugin by default:

    $ cat ~/.zshrc
    ...
    export NOSE_WITH_PYNOTIFY=1
    ...
    $ nosetests

License
-------
Copyright (c) 2011 Colin Drake

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
