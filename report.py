def report_bug(except_name: str, line_num: int, error_code: str):
    print(except_name + ':\n\tLine ' + str(line_num) + ': ' + error_code)
