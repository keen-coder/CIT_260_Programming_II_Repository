def message():
    print('I am Arthur,')
    print('King of the Britons.')

# In a more complex python program, it is always good to have a main / driver file which includes
# a main function followed by the if __name__ structure. The main() function should ALWAYS be
# where your program starts and it makes it easier for someone new to your code to dive in and begin
# to understand what is going on.



def main():
    # initialization code goes here, and then call whatever other functions necessary
    # for your program.
    message()


# WHY??? this if section??

# Every python file has a built-in variable called __name__
# When a python file is executed, the __name__ variable is set to something specific.
#   If the file is executed directly such as from a command-line using "python myscript.py", 
#   then __name__ is set to "__main__"
#   If the file is imported into another file using an import statement, then __name__ is set to
#   "the_module_name".
#       If I were to import this file 01_simple_function.py, then __name__ would be set to 
#       "01_simple_function".

# Why does this matter?
# If you write:
#   if __name__ == "__main__":
#       main()
#   That block will only run when you execute the file directly. It will not run when the file is imported.

# This is important when you want to import a python module that has a main method and you ONLY want to
# use functions in that module, and not execute the entire module.

if __name__ == "__main__":
    main()