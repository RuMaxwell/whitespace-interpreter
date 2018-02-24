from sys import argv

from storage import *
from io import *

# Stack used in the interpreter
main_stack = Stack()
# Heap storage used in the interpreter
main_heaps = Heaps()


def check_argv():
    """
    Check the arguments given by executing this python file.
    """
    if len(argv) == 1:
        pass  # run
    else:
        if argv[1] == 'run':
            pass  # run
        elif argv[1] == 'step':
            pass  # step
        elif argv[1] == 'debug':
            pass  # debug
        elif argv[1] == 'help':
            pass  # help
        else:
            pass


def main():
    pass


def run():
    """Directly run the script"""
    pass


def step():
    """Run the script step by step"""
    pass


def debug():
    """Run the script in debug mode"""
    pass


def usage_help():
    """Show the usage of arguments"""
    pass


def interpret_help():
    """Show how to use the interpreter"""
    pass


if __name__ == '__main__':
    main()
