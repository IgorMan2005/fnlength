# fnlength

<img src="https://igorman2005.github.io/images/fnlength.jpg" alt="fnlength">

Python filename length script.
The program enumerates the file in subdirectories and shortens long filenames to the specified number of characters.
function will create log file in top dir with name log_%Y%m%d.log

## Setup
https://pypi.org/project/fnlength/

**pip install fnlength**

## Example1:
```
import fnlength 

target = fnlength.fnlength()

# default 25
target.MAX_FILENAME_LENGTH = 30             

target.start()                              

```

## Example2:
```
from fnlength import FileNameLength

target = FileNameLength()

# default 25
target.MAX_FILENAME_LENGTH = 35

target.start()         

```

### Documentation

https://best-itpro.ru/news/fnlength/


