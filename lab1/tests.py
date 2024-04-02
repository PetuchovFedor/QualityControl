import sys
import subprocess

EXE_FILE_PATH = 'triangle.py'
RESULT_FILE_PATH = 'result.txt'
SUCCESS_MSG = 'success\n'
ERROR_MSG = 'error\n'

def run_tests(exe_file_path, test_case_path, output_path):
    input = open(test_case_path, encoding='utf-8', mode='r')
    output = open(output_path, 'w')
    for line in input:
        temp_list = line.rstrip('\n').split(sep=' ')
        args =  temp_list[0:temp_list.index('-')]
        args.insert(0, exe_file_path)
        args.insert(0, 'python')
        result = ' '.join(temp_list[temp_list.index('-') + 1:len(temp_list)])
        # print('r ', result)
        # print('args ', args)
        process = subprocess.run(args=args, capture_output=True, shell=True, text=True)
        # print('out ', process.stdout)
        cmdout = process.stdout.rstrip('\n')
        output.write(SUCCESS_MSG if result == cmdout else ERROR_MSG)
        # print(SUCCESS_MSG if result == cmdout else 'error\n')
    input.close()
    output.close()

args = sys.argv
args.pop(0)
run_tests(EXE_FILE_PATH, args[0], RESULT_FILE_PATH)