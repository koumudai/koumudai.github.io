import os
import shutil

def f(path):
    for e in os.listdir(f'{path}/'):
        if os.path.isdir(e): # 文件夹
            f(f'{path}/{e}')           
        else: # 文件
            if 'svg' in e and e[0] != '.':
                e_new = e.replace('svg', 'SVG')
                print(e)
                print(e_new)
                # shutil.move(f'{path}/{e}', f'{path}/{e_new}')
            elif 'png' in e and e[0] != '.':
                e_new = e.replace('png', 'PNG')
                print(e)
                print(e_new)
                # shutil.move(f'{path}/{e}', f'{path}/{e_new}')
            

f('.')