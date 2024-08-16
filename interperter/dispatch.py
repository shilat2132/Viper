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


def arrayMethodsDetails():
      dictionary= {
            "length": (0, "Number"),
            "index": (1, "Number"),
            "get": (1, "any"),
            "set": (2, None),
            "addItem": (2, None),
            "append": (1, None),
            "remove": (1, None)
      }
      return dictionary

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

def tuplesMethodsDetails():
      dictionary = {
            "getItem": (1, "any"),
            "combine": (1, "tuple"),
            "index": (1, "Number"),
            "sorted": (0, "tuple"),
            "length": (0, "Number")
      }
      return dictionary

def dispatchStringMethodsInit(dispatch):
      """
      updates dispatch with all tuple methods
      """
      for name in dir(strings):
            attr = getattr(strings, name)
            dispatch[name] = attr

def stringsDetailsMethods():
      dictionary = {
            "REPLACE": (2, "string"),
            "isUpper": (0, "boolean"),
            "isLower": (0, "boolean"),
            "CONCAT": (1, "string")
      }
      return dictionary

def dispatchBuiltInFunctionsInit(dispatch):
    """
    updates dispatch with all operators functions, 
        built in functions - print, min, max, sqrt, range
    """
    for name in dir(arithmetics):
        attr = getattr(arithmetics, name)
        dispatch[name] = attr
  
    for name in dir(keywords):
            attr = getattr(keywords, name)
            if name=="rangeTuple": name = "range"
            if name == "output": name="print"
            dispatch[name] = attr
    
    
