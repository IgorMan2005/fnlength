# filenamelength
'''
Python filename length script.
The program enumerates the file in subdirectories and shortens long filenames to the specified number of characters.
function will create log file in top dir with name log_%Y%m%d.log

Created by IgorMan, 2023
https://github.com/IgorMan2005/filenamelength
'''

import os
import datetime

class FileNameLength:

    def __init__(self):
        self.root_dir = os.getcwd()
        self.path = os.getcwd()
        self.level = 1
        self.MAX_FILENAME_LENGTH = 25
        self.start_time = datetime.datetime.now()
        self.log_file = self.root_dir + os.sep + 'log_' + str(self.start_time.strftime("%Y%m%d")) + '.log'
        self.log = 'Start time: ' + str(self.start_time.strftime('%d%m%Y %H:%M:%S')) + '\n'
        self.log = 'Log file: ' + self.log_file + '\n\n'
        
    def get_info(self):
        print(f'Root dir: {self.root_dir}')
        print(f'Log file: {self.log_file}')
        print(f'MAX_FILENAME_LENGTH: {self.MAX_FILENAME_LENGTH}')
        print()

    def save_logs(self):
        """
        Save log method
        """        
        with open(self.log_file, 'a', encoding='utf-8') as log_save:
            log_save.write(self.log)


    def start(self):
        """Check files name.

        Shows the names of files and it extensions in them for each directory in the directory 
        tree rooted at top (including top itself, but excluding '.' and '..')

        check_files_names(MAX_FILENAME_LENGTH=25, path=os.getcwd(), level=1)
        path  - by default os.getcwd(), current dir
        level - by default = 1, top level

        function will create log file in top dir with name log_%Y%m%d.log        
        """
        os.system('cls') if os.name == 'nt' else os.system('clear')     

        print('FILE NAME LETNGH')
        print('----------------')

        self.log = '\nMAX_FILENAME_LENGTH = ' + str(self.MAX_FILENAME_LENGTH) + '\n'
        print(self.log)
        # Log begin
        self.save_logs() 

        # Begin main program
        self.check_files_names()
    

    def check_files_names(self):
        """
        main program
        """
        self.log = ''

        self.log += '\nPath: ' + self.path
        self.log += '\nLevel: ' + str(self.level)
        self.log += '\nContent: ' + str(os.listdir(self.path)) + "\n\n"

        print(self.log)
        self.save_logs() 
        self.log = ''
        
        sep = os.sep
        path = self.path
        for i in os.listdir(self.path):            
            # check file name
            if os.path.isfile(path + sep + i):            
                if len(os.path.splitext(i)[0]) > self.MAX_FILENAME_LENGTH:
                    self.log += 'Filename: '+ str(os.path.splitext(i)[0]) + ' more then ' + str(self.MAX_FILENAME_LENGTH) + ' !\n'
                    print(self.log)

                    new_file_name = os.path.splitext(i)[0][0:self.MAX_FILENAME_LENGTH]
                    # check for file exists, if file with new name exist, new name wilk be new_name_%y%m%d_%H%M%S
                    if os.path.exists(path + sep + new_file_name + os.path.splitext(i)[1]):
                        self.log +='new_file_name ' + str(os.path.splitext(i)[1]) + ' exists...\n'
                        print(self.log)                        
                        new_file_name +=  str(datetime.datetime.now().strftime('_%y%m%d_%H%M%S')) + os.path.splitext(i)[1]
                        
                    try:
                        os.replace(path + sep + os.path.splitext(i)[0] + os.path.splitext(i)[1], path + sep + new_file_name)                    
                    except:
                        self.log += '\nError to copy ' + str(os.path.splitext(i)[0]) + str(os.path.splitext(i)[1]) + ' in ' + new_file_name + ' (!)\n'
                        print(self.log)
                    
                    self.log += 'New file name: ' + new_file_name + str(os.path.splitext(i)[1]) + '\n'
                    print(self.log)
                else:
                    self.log += 'File: ' + str(i) + ' - good name size\n'
                    print(self.log)


                self.save_logs() 
                self.log = ''

            # change dir
            if os.path.isdir(path + sep + i):
                self.save_logs() 
                self.path = path + sep + i
                self.level += 1
                self.check_files_names()
    

def main():
    os.system('cls') if os.name == 'nt' else os.system('clear') 
    print('FILE NAME LETNGH')
    print('----------------\n')

    # target = FileNameLength()    
    # target.start()
    

if __name__ == '__main__':    
    main()
    print('Install filenamelength (pip install filenamelength) and use it (import filenamelength) ;)\n')
    print('Documentation & Example: https://github.com/IgorMan2005/filenamelength\n')



