"""
Directories traversal
---------------------
Created by IgorMan, 2023
"""

import os

def dir_traversal(path=os.getcwd(), level=1):
    """Directories traversal.

    Shows the names of directories and files in them for each directory in the directory 
    tree rooted at top (including top itself, but excluding '.' and '..')

    dir_traversal(path=os.getcwd(), level=1)
    path  - by default os.getcwd(), current dir
    level - by default = 1, top level
    
    """
    print('\nDirectories traversal')
    print('---------------------')
    print(f'\nLevel: {level}.\nContent: {os.listdir(path)}')
    sep = os.sep
    for i in os.listdir(path):
        if os.path.isdir(path + sep + i):
            print('\nDown inside. ', path + sep + i)
            dir_traversal(path + sep + i, level + 1)
            print(f'\nBack in: {path}')

def main():

    os.system('cls') if os.name == 'nt' else os.system('clear') 
    print('Special for FileNameLength')
    print('--------------------------\n')
    print(f'Current path: {os.getcwd()}')

    while True:
        path = input('Input target dir. For using current, just press Enter: ')
        if path.strip() == '':
            path = os.getcwd()
            print(f'Ok! Use current: {path}\n')
            break
        else:
            if os.path.exists(path):
                if os.path.isdir(path):
                    break
            else:
                print('Check your dir and try again')

    print(path)
    dir_traversal(path, level=1)



if __name__ == '__main__':
    main()

