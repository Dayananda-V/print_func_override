# System Print Override Through Environment Flag 

This project helps you to control system print function override under control flag

Enable print function log on system console
```
$ export CUSTOM_DBG_FLAG=True 
```

Disable print function log on system console
```
$ export CUSTOM_DBG_FLAG=False
```

## Installation

```
$ git clone https://github.com/dayanandasiet/print_func_override.git
$ cd print_func_override
$ python setup.py install --user
```

## Use

```
import printd
printd.print("Welcome to system print function override under flag")
## or
from printd import print
print("Welcome to system print function override under flag")
```
