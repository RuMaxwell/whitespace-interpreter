from sys import argv

from storage import *
from interpret import *
from io import *

from platform import system
if system() == 'Windows':
    import win_unicode_console
    win_unicode_console.enable()

# Stack used in the interpreter
main_stack = Stack()
# Heap storage used in the interpreter
main_heaps = Heaps()

test_code_1 = 'push-1   \t\noutput-number\t\n \tend-program\n\n\n'
test_code_2 = '  \t \n  \t\t\n\t\n \t\n\n\n'


def check_argv():
    """
    Check the arguments given by executing this python file.
    """
    if len(argv) >= 2:
        source_filename = argv[-1]
        with open(source_filename, 'r') as read_file:
            source_code = read_file.readlines()
            source_code = ''.join(source_code)
            if len(argv) == 2:
                run(source_code)  # run
            else:
                if argv[1] in ['--run', '-r']:
                    run(source_code)  # run
                elif argv[1] in ['--show-steps', '-s']:
                    show_steps(source_code)  # show steps
                elif argv[1] == ['--step', '-p']:
                    step(source_code)  # step
                elif argv[1] == ['--debug', '-d']:
                    debug(source_code)  # debug
                elif argv[1] == ['--tutorial', '-t']:
                    usage_help()  # tutorial
                elif argv[1] == ['--help', '-h']:
                    interpret_help()  # help
                else:
                    print('Unknown option.')
                    interpret_help()
    else:
        pass


def main():
    check_argv()


def run(script):
    """Directly run the script"""
    script = strip_non_wsp(script)
    instructions = split_insts(script)
    execute_insts(instructions)


def show_steps(script):
    """Show each step of the script"""
    script = strip_non_wsp(script)
    instructions = split_insts(script)
    for inst in instructions:
        print(inst)


def step(script):
    """Run the script step by step"""
    pass


def debug(script):
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
