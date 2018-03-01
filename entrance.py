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

version = '0.0.1'


def show_version():
    global version
    print('Whitespace Interpreter, version ' + version)


def check_argv():
    """
    Check the arguments given by executing this python file.
    """
    if len(argv) >= 2:
        source_filename = argv[-1]
        try:
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
                    elif argv[1] in ['--step', '-p']:
                        step(source_code)  # step
                    elif argv[1] in ['--debug', '-d']:
                        debug(source_code)  # debug
                    elif argv[1] in ['--version', '-v']:
                        show_version()  # version
                    elif argv[1] in ['--tutorial', '-t']:
                        usage_help()  # tutorial
                    elif argv[1] in ['--help', '-h']:
                        interpret_help()  # help
                    else:
                        print('Unknown option.')
                        interpret_help()
        except FileNotFoundError:
            print('Fatal error: file ' + source_filename + ' not found')
    else:
        print('Fatal error: no input file')


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
