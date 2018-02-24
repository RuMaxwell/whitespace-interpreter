keywords = [' ', '\t', '\n']

test_source = 'push-1   \t\noutput-number\t\n \tend-program\n\n\n'


def strip_non_wsp(source):
    """Generate a string that only remains white-space character"""
    new_str = []
    source = list(source)
    for c in source:
        if c in keywords:
            new_str.append(c)
    # Join list into str
    return ''.join(new_str)


def split_inst(ws_source):
    """Split the whole source code (only white-spaces) into instructions"""
    insts = []
    read = 0
    line = 0
    column = 0
    inst_bg = 0
    inst_ed = 0

    try:
        while (read < len(ws_source)):
            # 1
            if ws_source[read] == ' ':
                # Stack manipulation
                inst_bg = read
                read += 1
                if ws_source[read] == ' ':
                    # Push
                    read += 1
                    # Read the operand
                    while ws_source[read] != '\n':
                        operand += ws_source[read]
                        read += 1
                    operand = bi_to_dec(operand, signed=True)

                    inst_ed = read
    except IndexError:
        # Report a bug
        print('Compilation error: not a complete instruction:\n\tLine ' + line + ', column ' + column\
              + ': ' + source[inst_bg: read + 1])


def execute_inst(instruction):
    """Execute an instruction"""
    pass


def bi_to_dec(bi_str, signed):
    """Change binary number (' ' and '\t' string) to decimal"""
    if signed:
        sign = bi_str[0]
        bi_str = bi_str[1:]
    else:
        sign = None

    dec = 0
    max_digit = len(bi_str)
    for i in range(max_digit):
        # dec += bi_str[i] == '\t' ? 1 * 2 ** (...) : 0
        dec += 1 * 2 ** (max_digit - i - 1) if bi_str[i] == '\t' else 0
    if sign != None:
        dec = dec if sign == ' ' else -dec
    return dec
