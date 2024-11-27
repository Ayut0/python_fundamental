import sys

# check all the expected errors
if len(sys.argv) < 2:
    sys.exit("missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("too many command-line arguments")

# Once you make sure you take care of all the errors, you can execute the code you really want to run
print("hello, my name is", sys.argv[1])