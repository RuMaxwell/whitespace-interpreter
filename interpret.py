from report import *

keywords = [' ', '\t', '\n']


def strip_non_wsp(source: str):
    """Generate a string that only remains white-space character"""
    new_str = []
    source = list(source)
    for c in source:
        if c in keywords:
            new_str.append(c)
    # Join list into str
    return ''.join(new_str)


def split_insts(ws_source: str):
    """
    Split the whole source code (only white-spaces) into instructions.
    It's like a compiler.

    MENTION: STRUCTURE SIMILAR FOR INSTRUCTION CHECKINGS
    """
    insts = []  # Instruction list
    read = 0    # The Location in ws_source
    line = 1    # The line number in ws_source
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
                    # 1 [s][s] Push
                    read, inst_ed = read_wth_oprd(1, ws_source, inst_bg, read, insts,
                                                  'Push stack (%s)', oprd_signed=True)
                    inst_bg = inst_ed
                    line += 1  # An operand should end with a '\n'
                elif ws_source[read] == '\n':
                    read += 1
                    line += 1
                    if ws_source[read] == ' ':
                        # 2 [s][n][s] Duplicate stack top
                        read, inst_ed = read_non_oprd(2, ws_source, inst_bg, read, insts,
                                                      'Duplicate stack top')
                        inst_bg = inst_ed
                    elif ws_source[read] == '\t':
                        # 3 [s][n][t] Swap top two on stack
                        read, inst_ed = read_non_oprd(3, ws_source, inst_bg, read, insts,
                                                      'Swap top two data on stack')
                        inst_bg = inst_ed
                    elif ws_source[read] == '\n':
                        # 4 [s][n][n] Pop stack
                        read, inst_ed = read_non_oprd(4, ws_source, inst_bg, read, insts, 'Pop stack')
                        inst_bg = inst_ed
                        line += 1
                elif ws_source[read] == '\t':
                    read += 1
                    if ws_source[read] == ' ':
                        # 5 [s][t][s] Duplicate the Nth data onto stack top
                        read, inst_ed = read_wth_oprd(5, ws_source, inst_bg, read, insts,
                                                      'Duplicate the Nth data onto stack top, where N = %s',
                                                      oprd_signed=True, disp_base=10)
                        line += 1  # An operand should end with a '\n'
                        inst_bg = inst_ed
                    elif ws_source[read] == '\n':
                        # 6 [s][t][n] Slide N data off stack
                        read, inst_ed = read_wth_oprd(6, ws_source, inst_bg, read, insts,
                                                      'Slide N data off stack, where N = %s',
                                                      oprd_signed=True, disp_base=10)
                        inst_bg = inst_ed
                        line += 1
                        line += 1  # An operand should end with a '\n'
                    else:
                        # Report a bug
                        report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                        read += 1
                        inst_bg = read
                else:
                    # Report a bug
                    report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                    read += 1
                    inst_bg = read
            elif ws_source[read] == '\t':
                inst_bg = read
                read += 1
                if ws_source[read] == ' ':
                    # Arithmetic [t][s]
                    read += 1
                    if ws_source[read] == ' ':
                        read += 1
                        if ws_source[read] == ' ':
                            # 7 Add [t][s][s][s]
                            read, inst_ed = read_non_oprd(7, ws_source, inst_bg, read, insts, 'Add')
                            inst_bg = inst_ed
                        elif ws_source[read] == '\t':
                            # 8 Subtract [t][s][s][t]
                            read, inst_ed = read_non_oprd(8, ws_source, inst_bg, read, insts, 'Subtract')
                            inst_bg = inst_ed
                        elif ws_source[read] == '\n':
                            # 9 Multiply [t][s][s][n]
                            read, inst_ed = read_non_oprd(9, ws_source, inst_bg, read, insts, 'Multiply')
                            inst_bg = inst_ed
                            line += 1
                        else:
                            # Report a bug
                            report_bug('Unknow instruction', line, ws_source[inst_bg: read + 1])
                            read += 1
                            inst_bg = read
                    elif ws_source[read] == '\t':
                        read += 1
                        if ws_source[read] == ' ':
                            # 10 Divide [t][s][t][s]
                            read, inst_ed = read_non_oprd(10, ws_source, inst_bg, read, insts, 'Divide')
                            inst_bg = inst_ed
                        elif ws_source[read] == '\t':
                            # 11 Modulo [t][s][t][t]
                            read, inst_ed = read_non_oprd(11, ws_source, inst_bg, read, insts, 'Modulo')
                            inst_bg = inst_ed
                        else:
                            # Report a bug
                            report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                            read += 1
                            inst_bg = read
                elif ws_source[read] == '\t':
                    # Heap access [t][t]
                    read += 1
                    if ws_source[read] == ' ':
                        # 12 Store [t][t][s]
                        read, inst_ed = read_non_oprd(12, ws_source, inst_bg, read, insts, 'Store')
                        inst_bg = inst_ed
                    elif ws_source[read] == '\t':
                        # 13 Retrieve [t][t][t]
                        read, inst_ed = read_non_oprd(13, ws_source, inst_bg, read, insts, 'Retrieve')
                        inst_bg = inst_ed
                    else:
                        # Report a bug
                        report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                        read += 1
                        inst_bg = read
                elif ws_source[read] == '\n':
                    read += 1
                    line += 1
                    # I/O control [t][n]
                    if ws_source[read] == ' ':
                        read += 1
                        if ws_source[read] == ' ':
                            # 14 Output stack top [Character] [t][n][s][s]
                            read, inst_ed = read_non_oprd(14, ws_source, inst_bg, read, insts,
                                                          'Output stack top [Character]')
                            inst_bg = inst_ed
                        elif ws_source[read] == '\t':
                            # 15 Output stack top [Number] [t][n][s][t]
                            read, inst_ed = read_non_oprd(15, ws_source, inst_bg, read, insts,
                                                          'Output stack top [Number]')
                            inst_bg = inst_ed
                        else:
                            # Report a bug
                            report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                            read += 1
                            inst_bg = read
                    elif ws_source[read] == '\t':
                        read += 1
                        if ws_source[read] == ' ':
                            # 16 Read to heap (addressed by stack top) [Character] [t][n][t][s]
                            read, inst_ed = read_non_oprd(16, ws_source, inst_bg, read, insts,
                                                          'Read to heap (addressed by stack top) [Character]')
                            inst_bg = inst_ed
                        elif ws_source[read] == '\t':
                            # 17 Read to heap (addressed by stack top) [Number] [t][n][t][t]
                            read, inst_ed = read_non_oprd(17, ws_source, inst_bg, read, insts,
                                                          'Read to heap (addressed by stack top) [Number]')
                            inst_bg = inst_ed
                        else:
                            # Report a bug
                            report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                            read += 1
                            inst_bg = read
                    else:
                        # Report a bug
                        report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                        read += 1
                        inst_bg = read
            elif ws_source[read] == '\n':
                inst_bg = read
                read += 1
                line += 1
                # Flow control [n]
                if ws_source[read] == ' ':
                    read += 1
                    line += 1
                    if ws_source[read] == ' ':
                        # 18 Set a label [n][s][s]
                        read, inst_ed = read_wth_oprd(18, ws_source, inst_bg, read, insts,
                                                      'Set a label <%s>', oprd_signed=False)
                        inst_bg = inst_ed
                        line += 1  # An operand should end with a '\n'
                    elif ws_source[read] == '\t':
                        # 19 Call the subroutine at the label [n][s][t]
                        read, inst_ed = read_wth_oprd(19, ws_source, inst_bg, read, insts,
                                                      'Call the subroutine at the label <%s>',
                                                      oprd_signed=False)
                        inst_bg = inst_ed
                        line += 1  # An operand should end with a '\n'
                    elif ws_source[read] == '\n':
                        # 20 Jump to the label unconditionally [n][s][n]
                        read, inst_ed = read_wth_oprd(20, ws_source, inst_bg, read, insts,
                                                      'Jump to the label unconditionally <%s>',
                                                      oprd_signed=False)
                        inst_bg = inst_ed
                        line += 1
                        line += 1  # An operand should end with a '\n'
                elif ws_source[read] == '\t':
                    if ws_source[read] == ' ':
                        # 21 Jump to the label if stack top is 0 [n][t][s]
                        read, inst_ed = read_wth_oprd(21, ws_source, inst_bg, read, insts,
                                                      'Jump to the label if stack top is 0 <%s>',
                                                      oprd_signed=False)
                        inst_bg = inst_ed
                        line += 1  # An operand should end with a '\n'
                    elif ws_source[read] == '\t':
                        # 22 Jump to the label if stack top is negative [n][t][t]
                        read, inst_ed = read_wth_oprd(22, ws_source, inst_bg, read, insts,
                                                      'Jump to the label if stack top is negative <%s>',
                                                      oprd_signed=False)
                        inst_bg = inst_ed
                        line += 1  # An operand should end with a '\n'
                    elif ws_source[read] == '\n':
                        # 23 End the subroutine [n][t][n]
                        read, inst_ed = read_non_oprd(23, ws_source, inst_bg, read, insts,
                                                      'End the subroutine')
                        inst_bg = inst_ed
                        line += 1
                elif ws_source[read] == '\n':
                    read += 1
                    line += 1
                    # 24 End the program [n][n][n]
                    read, inst_ed = read_non_oprd(24, ws_source, inst_bg, read, insts, 'End the program')
                    inst_bg = inst_ed
                    line += 1
            else:
                # Report a bug
                report_bug('Unknown instruction', line, ws_source[inst_bg: read + 1])
                read += 1
                inst_bg = read
    except IndexError:
        # Report a bug
        report_bug('Unknown instrution', line, ws_source[inst_bg: read + 1])
        read += 1
        inst_bg = read

    return insts


def read_non_oprd(id: int, ws_source: str, inst_bg: int, read: int, insts: list, descrip: str):
    """
    Read the whole non-operand instruction.
    Parameters are named the same as which in function split_inst.
    :param descrip: Brief description about what the instruction does
    :return: read, inst_ed
    """
    read += 1
    inst_ed = read
    # Append instruction list
    insts.append((id, ws_source[inst_bg: inst_ed], descrip))
    return read, inst_ed


def read_wth_oprd(id: int, ws_source: str, inst_bg: int, read: int, insts: list, descrip: str,
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
    oprd_ed = read
    operand = bi_to_dec(ws_source[oprd_bg: oprd_ed], signed=oprd_signed)
    read += 1
    inst_ed = read
    # Append instruction list
    if disp_base == 10:
        insts.append((id, ws_source[inst_bg: inst_ed], descrip % str(operand)))
    elif disp_base == 16:
        insts.append((id, ws_source[inst_bg: inst_ed], descrip % hex(operand)))
    return read, inst_ed


def execute_inst(instruction: str):
    """Execute an instruction"""
    pass


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
