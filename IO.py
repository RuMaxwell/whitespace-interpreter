def read_file(file):
    """
    Read all characters in a file.
    :param file: absolute path to the file
    :return: the content
    """
    with open(file, mode='r') as code:
        script = code.readlines()
    return script


def get_input(mode):
    """
    Get an input from the console.
    INSTRUCTION: [t][n][t][s] or [t][n][t][t]. Part of the execution.
    :param mode: 'number' or 'character'
    :return: the input
    """
    value = input('Program requires an input of' + mode)
    if mode == 'number':
        try:
            res = int(value)
            return res
        except ValueError:
            print('Not a valid input of a number.')
    elif mode == 'character':
        try:
            res = ord(value[0])
            return res
        except TypeError:
            print('Not a valid input of a character.')
    else:
        raise ValueError('get_input: No such mode.')


def make_output(mode, value):
    """
    Make an output to the console.
    :param mode: 'number' or 'character'
    :param value: stack top which just had been popped
    """
    if mode == 'number':
        print(value)
    elif mode == 'character':
        print(chr(value))
    else:
        raise ValueError('make_output: No such mode.')
