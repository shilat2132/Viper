import sys
import os
# import inspect

original_sys_path = sys.path.copy()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))

import arrays
import keywords
import strings
import tuples
import arithmetics
sys.path = original_sys_path

def dispatchArrayMethodsInit(dispatch):
    """
    updates dispatch with all array methods
    """
    attr = getattr(arrays, "Array")
    dispatch["Array"] = attr
    for name in dir(arrays.Array):
            attr = getattr(arrays.Array, name)
            dispatch[name] = attr

def dispatchTupleMethodsInit(dispatch):
    """
    updates dispatch with all tuple methods
    """
    attr = getattr(tuples, "Tuple")
    dispatch["Tuple"] = attr
    for name in dir(tuples.Tuple):
            attr = getattr(tuples.Tuple, name)
            dispatch[name] = attr

    


def dispatchBuiltInFunctionsInit(dispatch):
    """
    updates dispatch with all operators functions, 
        built in functions - like print, min
        and keywords functions while/for/if
    """
    for name in dir(arithmetics):
        attr = getattr(arithmetics, name)
        dispatch[name] = attr
  
    for name in dir(keywords):
            attr = getattr(keywords, name)
            if name=="rangeTuple": name = "range"
            if name == "output": name="print"
            dispatch[name] = attr
    
    for name in dir(strings):
            attr = getattr(strings, name)
            dispatch[name] = attr
