import os
import shutil

def f(path):
    print(path)
    for e in os.listdir(f'{path}/'):
        if os.path.isdir(e): # 文件夹
            f(f'{path}/{e}')           
        else: # 文件
            if 'svg' in e and e[0] != '.':
                e_new = e.replace('svg', 'SVG')
                print(e, e_new)
                # shutil.move(f'{path}/{e}', f'{path}/{e_new}')
            elif 'png' in e and e[0] != '.':
                e_new = e.replace('png', 'PNG')
                print(e, e_new)
                # shutil.move(f'{path}/{e}', f'{path}/{e_new}')
            elif 'SVG1' in e and e[0] != '.':
                e_new = e.replace('SVG1', 'SVG')
                print(e, e_new)
                shutil.move(f'{path}/{e}', f'{path}/{e_new}')
                # shutil.move(f'{path}/{e_new}', f'{path}/{e}')
            elif 'PNG1' in e and e[0] != '.':
                e_new = e.replace('PNG1', 'PNG')
                print(e, e_new)
                shutil.move(f'{path}/{e}', f'{path}/{e_new}')
                # shutil.move(f'{path}/{e_new}', f'{path}/{e}')
            
            
f('.')