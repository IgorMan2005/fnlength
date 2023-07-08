# Example using filenamelength
'''
Python filename length script.
The program enumerates the file in subdirectories and shortens long filenames to the specified number of characters.
function will create log file in top dir with name log_%Y%m%d.log

Created by IgorMan, 2023
https://github.com/IgorMan2005/fnlength 
'''
from fnlength import FileNameLength

target = FileNameLength()

# default 25
target.MAX_FILENAME_LENGTH = 35

target.start()                              










