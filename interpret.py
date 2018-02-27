from report import *

keywords = [' ', '\t', '\n']

test_source = 'push-1   \t\noutput-number\t\n \tend-program\n\n\n'


def strip_non_wsp(source: str):
    """Generate a string that only remains white-space character"""
    new_str = []
    source = list(source)
    for c in source:
        if c in keywords:
            new_str.append(c)
    # Join list into str
    return ''.join(new_str)


def visualize(ws_source: str):
    """Use [s][t][n] to comment a white-space source code"""
    ws_source.replace(' ', '[s] ')
    ws_source.replace('\t', '[t]\t')
    ws_source.replace('\n', '[n]\n')


def split_inst(ws_source: str):
    """
    Split the whole source code (only white-spaces) into instructions.
    It's like a compiler.

    MENTION: STRUCTURE SIMILAR FOR INSTRUCTION CHECKINGS
    """
    insts = []  # Instruction list
    read = 0    # The Location in ws_source
    line = 0    # The line number in ws_source
    inst_bg = 0 # The begin point of an instruction
    inst_ed = 0 # The end point of an instruction

    try:
        while (read < len(ws_source)):
            # 1
            if ws_source[read] == ' ':
                # [s] Stack manipulation
                inst_bg = read
                read += 1
                if ws_source[read] == ' ':
                    # 0 [s][s] Push
                    read, inst_ed = read_wth_oprd(ws_source, inst_st, read, insts,
                                                  'Push stack (%s)', oprd_signed=True)
                elif ws_source[read] == '\n':
                    read += 1
                    if ws_source[read] == ' ':
                        # 1 [s][n][s] Duplicate stack top
                        read, inst_ed = read_non_oprd(ws_source, inst_st, read, insts, 'Duplicate stack top')
                    elif ws_source[read] == '\t':
                        # 2 [s][n][t] Swap top two on stack
                        read, inst_ed = read_non_oprd(ws_source, inst_st, read, insts, 'Swap top two data on stack')
                    elif ws_source[read] == '\n':
                        # 3 [s][n][n] Pop stack
                        read, inst_ed = read_non_oprd(ws_source, inst_st, read, insts, 'Pop stack')
                elif ws_source[read] == '\t':
                    read += 1
                    if ws_source[read] == ' ':
                        # 4 [s][t][s] Duplicate the Nth data onto stack top
                        read, inst_ed = read_wth_oprd(ws_source, inst_st, read, insts,
                                                      'Duplicate the Nth data onto stack top, where N = %s',
                                                      oprd_signed=True, disp_base=10)
                    elif ws_source[read] == '\n':
                        # 5 [s][t][n] Slide N data off stack
                        read, inst_ed = read_wth_oprd(ws_source, inst_st, read, insts,
                                                      'Slide N data off stack, where N = %s',
                                                      oprd_signed=True, disp_base=10)
                    else:
                        # Report a bug
                        report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
    except IndexError:
        # Report a bug
        report_bug('Not a complete instruction', line, ws_source[inst_bg: read + 1])


def read_non_oprd(ws_source: str, inst_bg: int, read: int, insts: list, descrip: str):
    """
    Read the whole non-operand instruction.
    Parameters are named the same as which in function split_inst.
    :param descrip: Brief description about what the instruction does
    :return: read, inst_ed
    """
    read += 1
    inst_ed = read
    # Append instruction list
    insts.append((1, ws_source[inst_bg: inst_ed], descrip))
    return read, inst_ed


def read_wth_oprd(ws_source: str, inst_bg: int, read: int, insts: list, descrip: str,
                  oprd_signed: bool, disp_base=16):
    """
    Read the whole with-operand instruction.
    Parameters are named the same as which in function split_inst.
    :param descrip: A format string. Brief description about what the instruction does.
        A '%s' will be replaced by the operand
    :param oprd_signed: Bool, determine whether the operand is interpreted as a signed integer
    :param disp_base: Number base to displayed (10: decimal, 16: hexadecimal)
    :return: read, inst_ed
    """
    read += 1
    # Read to the end of the operand
    oprd_bg = read
    while ws_source[read] != '\n':
        read += 1
    # After while loop inst_ed is next to '\n'
    oprd_ed = inst_ed = read
    operand = bi_to_dec(ws_source[oprd_bg: oprd_ed], signed=oprd_signed)
    # Append instruction list
    if disp_base == 10:
        insts.append((0, ws_source[inst_bg: inst_ed], descrip % str(operand)))
    elif disp_base == 16:
        insts.append((0, ws_source[inst_bg: inst_ed], descrip % hex(operand)))
    return read, inst_ed


def execute_inst(instruction: str):
    """Execute an instruction"""
    # Read the operand
    while ws_source[read] != '\n':
        # operand += ws_source[read]
        read += 1
    # operand = bi_to_dec(operand, signed=True)


def execute_insts(inst_list: list):
    """Execute instructions"""
    pass


def bi_to_dec(bi_str: str, signed: bool):
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
