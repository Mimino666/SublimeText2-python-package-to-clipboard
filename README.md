SublimeText2-python-package-to-clipboard
========================================

Simple plugin to Sublime Text 2 editor to copy the Python package path of working file to clipboard.

Install
=======

The easiest way to install this is with [Package Control](http://wbond.net/sublime_packages/package_control).

Usage
=====

To copy the python package of working file press `Ctrl+Shift+C`. Note: it only works if the file's extension is .py.

Suppose the following directory tree of your Python project:

    x.py
    A/
      __init__.py
      y.py
      B/
        __init__.py
        z.py
      
Depending on the current working file, the following package names will be stored in clipboard:

    (current working file)  ->  (package name copied to clipboard)
    
    x.py                    ->  x
    y.py                    ->  A.y
    z.py                    ->  A.B.z
    A/__init__.py           ->  A
    A/B/__init__.py         ->  A.B
