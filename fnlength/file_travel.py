"""
Files traversal
-------------------
Created by IgorMan, 2023
"""

import os

def files_traversal(path=os.getcwd(), level=1):
    """Files traversal.

    Shows the names of files and it extensions in them for each directory in the directory 
    tree rooted at top (including top itself, but excluding '.' and '..')

    files_traversal(path=os.getcwd(), level=1)
    path  - by default os.getcwd(), current dir
    level - by default = 1, top level
    
    """
    print('\nFiles traversal')
    print('---------------')
    print(f'\nLevel: {level}.\nContent: {os.listdir(path)}')
    sep = os.sep
    for i in os.listdir(path):
        if os.path.isfile(path + sep + i):
            print(f'File: {i} | name: {os.path.splitext(i)[0]} | extension: {os.path.splitext(i)[1]}')
        if os.path.isdir(path + sep + i):            
            files_traversal(path + sep + i, level + 1)
            

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
    files_traversal(path, level=1)



if __name__ == '__main__':
    main()

