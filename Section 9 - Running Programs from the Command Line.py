#! python3
# Shebang Line should be the first thing in a file when it's being used

# Section 9, lesson 22
# Launching Python from Outside IDLE
# Here's where we move from basic stuff to running actual programs we create!


# Strictly speaking, you don't NEED the shebang line on Windows, but it does specify which version of Python to use,
# so, best to include it anyway.

print('Hello World')

#Ways to run the program:
# 1)
# Open the command prompt in the folder and use py.exe 'C:\...\...Section 9 - Running Programs from the Command Line.py'
# to execute.

# 2)
# Windows Run, supply py.exe 'C:\...\...Section 9 - Running Programs from the Command Line.py'
# Be mindful that the window will close immediately after it's done, so this program will flash very briefly and be gone.

# 3)
# Using a batch file. One example is created, in the directory called 'Section 9.bat'

# The batch file looks like this:
# @py "C:\Users\chris.prunotto\PycharmProjects\ATBS-Python\Section 9 - Running Programs from the Command Line.py" %*
# @pause

# The file path is enclosed in double quotes because it contains spaces.
# the %* tells windows to forward any command line arguments to the program (to be explained at a later
# time in the book)
# @pause tells the program to pause so it doesn't disappear.

# Note that since this is an absolute path reference, it won't work if that isn't the exact file path to the program.
# If a program has no output to the screen, @pyw can be used for a "windowless python" mode that is silent. Using it
# without @pause will make it mostly invisible.

# You can also add the project file to the PATH variables list to make execution more convenient, too, otherwise just
# double-clicking the batch file is enough.


# to note: commands are supplied when running the program, for instance when using Run, you would run it as:
# py.exe '...filepath.py' arg1 arg2 arg3
# space delimited, without commas, etc. which is why the %* is necessary.