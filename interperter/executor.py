import sys
import os
original_sys_path = sys.path.copy()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../utils')))
from arrays import Array
from tuples import Tuple
sys.path = original_sys_path


from vars import Vars, Variable
from functions import FunctionManager
from dispatch import *
def returnInstance(value):
    """
    returns the type of the value
    """
    if isinstance(value, int) or isinstance(value, int):
        return "Number"
    if isinstance(value, bool): return "boolean"
    if isinstance(value, Array): return "array"
    if isinstance(value, Tuple): return "tuple"
    if isinstance(value, str): return "string"


class Executor:

    builtInFunctions, arrayMethods, tupleMethods, stringMethods = FunctionManager(), FunctionManager(), FunctionManager(), FunctionManager()
    dispatchBuiltInFunctionsInit(builtInFunctions)
    dispatchArrayMethodsInit(arrayMethods)
    dispatchTupleMethodsInit(tupleMethods)
    dispatchStringMethodsInit(stringMethods)
    arraysMethodsDetails = arrayMethodsDetails()
    tuplesMethodsDetails = tuplesMethodsDetails()
    stringsDetailsMethods = stringsDetailsMethods()
   
    def __init__(self):
        self.vars = Vars()

    def evaluateFunctionCall(self, node):
        """
                evaluates and executes the function call,
                if the function doesn't exist - it raises an error
                Returns:
                    tuple:
                        - type of the returned value
                        - return value
        """
        funcName = node.value
        argsNode = node.children[0]
        argsList = [a.value if a.type!="var" else self.vars[a.value].value for a in argsNode.children]

        # key = function name, value= a tuple 
            # where the first element is the number of arguments the function takes (-1 refers to unlimited numner of args)
            # second element is the type of the element the function returns
        functionDetailsDict = {"sqrt": (1, "Number"),
                         "min": (2, "Number"),
                         "max": (2, "Number"),
                         "range": "tuple",
                         "print": (-1, "None")
                         }
        
        if funcName =="range":
            argsList.reverse() #custom range gets parameters in the order of (end, start) so reverse the order
            if len(argsList)>2 or len(argsList)<1 :
                raise TypeError (f"range() takes 1 up to 2 positional arguments but {len(argsList)} were given")
            returnType = functionDetailsDict[funcName]

        else:
            returnType = functionDetailsDict[funcName][1]
            if funcName!="print":
                numOfArgs = functionDetailsDict[funcName][0]
                if len(argsList)!=numOfArgs :
                    raise TypeError(f"{funcName}() takes {numOfArgs} positional elements but {len(argsList)} were given")

        value = Executor.builtInFunctions[funcName](*argsList)
    
        return returnType, value
    
    def evaluateMethods(self, node, isMethod=True, obj =None):
        """
            evaluates and executes a method call on a string/tuple/array or initializes array/tuple
            
            Params:
                node= the methodCall ASTnode
                isMethod = is that a method or initialization
                obj = the object the method should be called on(the name of the object)
            
            Errors:
                raises an error if method doesn't exist on the object type or if method got unmatched number of arguments

            Returns:
                tuple:
                    -returnType: type of the method returned element
                    - value: the result of the method call

        """
        typeDict ={"array":(Executor.arrayMethods, Executor.arraysMethodsDetails), 
                   "tuple": (Executor.tupleMethods, Executor.tuplesMethodsDetails), 
                   "string": (Executor.stringMethods, Executor.stringsDetailsMethods)}
        
        # gets the method name and the arguments
        methodName = node.value if isMethod else node.type
        valuesNode = node.children[0] if not isMethod else node.children[1]
        valuesList = [v.value if v.type!="var" else self.vars[v.value].value for v in valuesNode.children]
        
       
       
        # INITIALIZATION OF ARRAY/TUPLE
        if not isMethod: 
            if methodName=="Array":
                returnType = "array"
                methodsDict = Executor.arrayMethods
            else: 
                returnType = "tuple"
                methodsDict = Executor.tupleMethods
            value = methodsDict[methodName](*valuesList)

        # METHODS THAT AREN'T INITIALIZATION
        else:
            obj = self.vars[obj]
            instance = obj.type

            if instance not in ["array", "tuple", "string"]:
                raise TypeError(f"can't perform a method on object with type of {instance}")
            # checks for validation of number of arguments
            methodDetailsDict = typeDict[instance][1] 
            if methodName not in methodDetailsDict:
                raise TypeError(f"{instance} doesn't have {methodName} method")
            numOfArgs =  methodDetailsDict[methodName][0]
            if len(valuesList) !=numOfArgs:
                raise TypeError(f"{methodName}() takes {numOfArgs} positional elements but {len(valuesList)} were given")
           
            # execute the method
            methodsDict = typeDict[instance][0]
            value = methodsDict[methodName](obj.value, *valuesList)

            # checks the return type
            returnType = methodDetailsDict[methodName][1]
            if returnType=="any":
                returnType = returnInstance(value)
        return returnType, value



    
    def evaluateCondition(self, node):
        """
        Evaluates condition, raise an error if it's not bool and not a variable
            Args:
                node- the node whose condition needs to be evaluated
            Returns:
                condition- the boolean condition/variable
        """
        condType, condition, isVar = self.evaluateExp(node.children[0])
        # condition can be either a logical expression (resulting in boolean value) or a variable
        if condType != "boolean" and not isVar:
            raise TypeError("if and while should be followed only by a logical expression or a single variable")
        return condition
    

    def evaluateTerm(self, node):
        """
        Evaluates a term, which might be a literal, a variable, a function call, or a method call.

        Returns:
            tuple:
                - returnType (str): The type of the term's result.
                - value (Any): The value of the evaluated term.
                - isVar (bool): the returned element is var or not
        """
        returnType, value, isVar = None, None, False

        #literal
        if node.type in ["Number", "boolean", "string"]:
            returnType, value= node.type, node.value
        
        if node.type in ["Array", "Tuple"]:
            #  calls evaluate method to initialize new array/tuple
             returnType, value= self.evaluateMethods(node, False)
        
        # variable
        if node.type == "var":
            var = self.vars[node.value] #would raise an error if the variable doesn't exist
            isVar = True
            returnType, value = var.type, var.value
        
        # function call
        if node.type == "functionCall":
            returnType, value = self.evaluateFunctionCall(node)

        # METHOD CALL
        if node.type == "methodCall":
            returnType, value = self.evaluateMethods(node,True, node.children[0].value)
        return returnType, value, isVar
    
    

    def evaluateExp(self, node):
        """
            Evaluate an expression, either arithmetic or logic, 
            if the node isn't an expression it would call evaluateTerm method

            Returns:
               tuple:
                - returnType (str): the type of the expression's final result.
                - value (Any): The value of the evaluated expression.
                - isVar (bool): the returned element is var or not
        """
        isVar = False #used for logical expression in which one variable would also be considered as a logical expression - true if it's not None
       
        # arithmetic or logical
        if node.type == "arithmeticExp" or node.type =="logicalExp":
            operation = node.value
            returnType = "Number" if node.type == "arithmeticExp" else "boolean"
            if operation =="negate":
                op1 =self.evaluateExp(node.children[0])
                result = Executor.builtInFunctions[operation](op1[1]) #the value
                value = result
            else:   
                op1 = self.evaluateExp(node.children[0])
                op2 = self.evaluateExp(node.children[1])
                # op1 and op2 are both tuples whose second element is the value of the operand
                result = Executor.builtInFunctions[operation](op1[1], op2[1]) #the value
                value = result
        

        # if the node is not an expression then it's a term
        else:
            returnType, value, isVar = self.evaluateTerm(node)

        return returnType, value, isVar
    
    def evaluateStatement(self, node):
        """
        evaluate and execute (recursively if needed) the node (subtree) of the ast
         analyzes any possible construct of the code (any possible ast node)
        """
        # assign
        if node.type == "assign":
            target = node.children[0].value #the name of the target var
            source = self.evaluateExp(node.children[1]) #returns a tuple of type and value
            self.vars[target] = Variable(target, source[0], source[1])

        # if statement
        if node.type == "if":
            condition = self.evaluateCondition(node)
            if condition:
                self.evaluate(node.children[1])
            else:
                if len(node.children)==3: #if there is an else block
                    elseNode = node.children[2]
                    self.evaluate(elseNode.children[0])


        # while
        # first child = condition, second= body (subtree with statements nodes as children)
        if node.type == "while":
            condition = self.evaluateCondition(node)
            while condition:
                self.evaluate(node.children[1])
                condition = self.evaluateCondition(node)

        # for
        if node.type =="for":
            key = node.children[0].value #iteration variable name
            iterableNode = node.children[1] #the node of the iterable object
            bodyNode = node.children[2] #the for block statements
            currentElementType = None

            # iterable of range
            if iterableNode.value == "range":
                result = self.evaluateFunctionCall(iterableNode) #execute the range function
                iterable = result[1] #the tuple returned from range
                currentElementType = "Number" #each of the range elements is a number

            # ALSO CHECK FOR A TUPLE/ARRAY LITERAL
            if iterableNode.type in ["Array", "Tuple"]:
                returnType, iterable= self.evaluateMethods(iterableNode, "Array" if iterableNode.type=="Array" else "Tuple", False)
                
            # iterable of array/tuple variable
            if iterableNode.type =="identifier":
                iterable = self.vars[iterableNode.value].value
                iterType = returnInstance(iterable)
                if iterType not in ["array", "tuple"]:
                    raise TypeError(f"can't iterate over a non-iterable object {iterableNode.value}")
            
            self.vars[key]= Variable(key, None, None)
            for i in iterable:
                self.vars[key].value = i
                currentElementType = returnInstance(i)
                self.vars[key].type = currentElementType
                self.evaluate(bodyNode)
            del self.vars[key] #kill the key variable at the end of the scope


        # function call
        if node.type == "functionCall":
            self.evaluateFunctionCall(node)

        # method call
        if node.type =="methodCall":
            self.evaluateMethods(node, True, node.children[0].value)




    def evaluate(self, ast):
        """
        evaluate and executes the AST 
        """
        for child in ast.children:
            self.evaluateStatement(child)
        return self.vars

