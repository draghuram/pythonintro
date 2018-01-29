
Operating System Concepts
=========================

It is very useful to learn some operating system level concepts as
they will help you in understanding Python programs better. 

An operating system is a type of program that runs directly on the
hardware and makes other applications like Python possible to
run. Some examples of OS include: `Linux`, `Windows`, `MacOS`, `iOS`,
`Android` etc.


Shells
------

When you login into a machine, a program called `shell` is
started. The most popular shell on `Linux` is called `bash`. Shells
primarily do the following in an infinite loop:

- Wait for user to enter a command

- Run the command

For example, on PythonAnywhere_, a kind of Linux machine is
created for each user and when you get a `bash console`, you are logging
into this machine and `bash` is started for you where you can enter
commands. 

Some useful Commands
--------------------

- ``ls`` - lists files and folders

- ``cp`` - copies files and folders

- ``mv`` - renames files and folders

- ``rm`` - removes files and folders

- ``ps`` - shows running processes

Command components
------------------

- A command (or program) has mainly three components:

  - program name
  - options
  - arguments or parameters

- You can access all this information in your python program.

For example, you can access command line parameters using the list
``sys.argv``.

Command options
---------------

- All commands support options that change their behavior.

- Examples

  - `ls -l`, `ls -ltr`. Lists detailed information for files.

  - `cp -i`. Warns you if you are overwriting a file.

  - `mv -i`, `rm -i`. Same as above.

  - `rm -r`. Removes directories and any files with in those
    directories as well.


Command line parameters
-----------------------

- You can pass information to programs using command line parameters.

- If the values have spaces in them, place single or double quotes
  around the values.

Editors
-------

- Editors are programs that you use to create and modify files. 

- There are hundreds of editors available. Some examples:

  - `vi`, `emacs`
  - editor on PythonAnywhere_ site

- Editors support `syntax highlighting` where different language
  features are shown in different colors.

.. _PythonAnywhere: https://www.pythonanywhere.com

