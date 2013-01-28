SublimeText2-python-package-to-clipboard
========================================

Simple plugin to Sublime Text 2 editor to copy the Python package path of the working file to clipboard.

Install
=======

The easiest way to install this is with [Package Control](http://wbond.net/sublime_packages/package_control).

Usage
=====

To copy the Python package path of the working file press <kbd>Ctrl+Shift+C</kbd> or select an option from the context menu
(`right-click` somewhere in the text area of the working file).


Note: to specify which files should be considered as "Python files" you can edit "python_extensions" variable
in the settings.

Example
=======

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
