import sys
import os
import inspect

# Add the parent directory of 'utils' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))

import arrays
import blocks
import strings
import tuples
import arithmetics

def dispatchInit(dispatch):
    for name in dir(arithmetics):
            attr = getattr(arithmetics, name)
            dispatch[name] = attr
    for name in dir(arrays):
            attr = getattr(arrays, name)
            dispatch[name] = attr
    for name in dir(blocks):
            attr = getattr(blocks, name)
            dispatch[name] = attr

    for name in dir(tuples):
            attr = getattr(tuples, name)
            dispatch[name] = attr
    
    for name in dir(strings):
            attr = getattr(strings, name)
            dispatch[name] = attr