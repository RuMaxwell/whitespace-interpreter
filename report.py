def report_bug(except_name: str, line_num: int, error_code: str):
    error_code = visualize(error_code)
    print(except_name + ':\n\tLine ' + str(line_num) + ': ' + error_code)


def visualize(ws_source: str):
    """Use [s][t][n] to comment a white-space source code"""
    ws_source = ws_source.replace(' ', '[s] ')
    ws_source = ws_source.replace('\t', '[t]\t')
    ws_source = ws_source.replace('\n', '[n]\n')
    return ws_source
