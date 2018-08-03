import os
try:
    import __builtin__
except ImportError:
    # Python 3
    import builtins as __builtin__

def print(*args, **kwargs):
    if 'True' == os.getenv('CUSTOM_DBG_FLAG', 'False'):
        __builtin__.print(*args, **kwargs)