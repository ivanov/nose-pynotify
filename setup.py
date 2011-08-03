from setuptools import setup

setup(
    name="nose-pynotify",
    version="0.1",
    author="Colin Drake",
    author_email = "colin.f.drake@gmail.com",
    description = "Plugin for nose to use pynotify for graphical notifications",
    license = "BSD",
    py_modules = ["nose_pynotify"],
    entry_points = {
        "nose.plugins.0.10": [
            "pynotify = nose_pynotify:PyNotify"
            ]
        }
    )
