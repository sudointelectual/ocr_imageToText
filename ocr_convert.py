import os
import subprocess
from time import sleep


# --------- flatten and launch
def zen(args):
    args_list = flatten(args)
    inputs = subprocess.check_output(x for x in args_list)
    r_output = inputs.decode('utf-8').strip()
    output = []
    for x in r_output.split(','):
        output.append(x.strip())
    print(output)
    return output


def flatten(_list):
    flat_list = []
    for item in _list:
        if type(item) is list:
            for item in item:
                flat_list.append(item)
        else:
            flat_list.append(item)
    return flat_list


action = ['zenity', '--file-selection']
output = zen(action)

txt_path = '/path/to/output'

os.system(f'tesseract {output[0]} {txt_path}')
