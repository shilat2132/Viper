from vars import Vars, Variable
from functions import FunctionManager
from dispatch import dispatchBuiltInFunctionsInit, dispatchArrayMethodsInit, dispatchTupleMethodsInit

class Executor:

    builtInFunctions, arrayMethods, tupleMethods = FunctionManager(), FunctionManager(), FunctionManager()
    dispatchBuiltInFunctionsInit(builtInFunctions)
    dispatchArrayMethodsInit(arrayMethods)
    dispatchTupleMethodsInit(tupleMethods)

   
    def __init__(self):
        self.vars = Vars()
        self.userFunctions = FunctionManager()

    def evaluateFunctionCall(self, node):
        """
                evaluates and executes the function call,
                if the function isn't built in and not defined by user - it raises an error
                Returns:
                    tuple:
                        - type of the returned value
                        - return value
        """
        returnType, value = None, None
        funcName = node.value
        argsNode = node.children[0]
        argsList = [a.value if a.type!="var" else self.vars[a.value].value for a in argsNode.children ]
        if funcName in ["sqrt", "min", "max"]:
            returnType = "Number"
            value = Executor.builtInFunctions[funcName](*argsList)
        elif funcName in ["range", "print"]:
            if funcName == "range":
                returnType = "tuple"
                argsList.reverse() #custom range gets parameters as end, start so reverse the order
                if len(argsList)>2 or len(argsList)<1 :
                    raise TypeError ("range() takes 1 up to 2 positional arguments")
            value = Executor.builtInFunctions[funcName](*argsList)
    
        else:
            # after evaluating a func definition, take care of its return type and valus
            self.userFunctions[funcName](*argsList) #raises an error if function doesn't exist
        return returnType, value
    
    # need to check return type for any possible array/tuple method - maybe put it in a dictionary to make it easier
    def evaluateMethods(self, node, isArray=True, isMethod=True):
        """
            Params:
                node=
                isArray = is that an array's method or a tuple's
                isMethod = is that a method or initialization 
        """
        returnType, value = "array" if isArray else "tuple", None
        funcName = node.value if isMethod else node.type
        valuesNode = node.children[0]

        # NEED TO CHECK IF IT HAVE CHILDREN

        valuesList = [v.value if v.type!="var" else self.vars[v.value].value for v in valuesNode.children ]
        methodsDict = Executor.arrayMethods if isArray else Executor.tupleMethods
        if not isMethod:
            value = methodsDict[funcName](valuesList)

        # NEEDS TO TAKE CARE OF METHODS THAT AREN'T INITIALIZATION
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
            raise TypeError("if should be followed only by a logical expression")
        return condition
    

# needs to take care of method call later, also arrays and tuples
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
             returnType, value= self.evaluateMethods(node, True if node.type=="Array" else False, False)
        # variable - raises an error if variable doesn't exist
        if node.type == "var":
            var = self.vars[node.value]
            isVar = True
            returnType, value = var.type, var.value
        
        # function call - either built in or a user defined
        if node.type == "functionCall":
            returnType, value = self.evaluateFunctionCall(node)
        return returnType, value, isVar
    
        # MISSING A METHOD CALL AS A TERM EVALUATION
    

    def evaluateExp(self, node):
        """
            Evaluate an expression, either arithmetic or logic.

            Returns:
               tuple:
                - returnType (str): the type of the expression's final result.
                - value (Any): The value of the evaluated expression.
                - isVar (bool): the returned element is var or not
        """
        isVar = False
        # arithmetic or logical
        if node.type == "arithmeticExp" or node.type =="logicalExp":
            operation = node.value
            returnType = "Number" if node.type == "arithmeticExp" else "boolean"
            op1 = self.evaluateExp(node.children[0])
            op2 = self.evaluateExp(node.children[1])
            result = Executor.builtInFunctions[operation](op1[1], op2[1]) #the value
            value = result
        

        # term
        else:
            returnType, value, isVar = self.evaluateTerm(node)

        return returnType, value, isVar
    
    def evaluateStatement(self, node):
        """
        evaluate and execute (recursively if needed) the node (subtree) of the ast
         analyzes any possible construct of the code (any possible ast node)
        """
        # assign
        # don't forget to allow function/method call
        if node.type == "assign":
            target = node.children[0].value #the name of the target var
            source = self.evaluateExp(node.children[1]) #returns a tuple of type and value
            self.vars[target] = Variable(target, source[0], source[1])

        # if statement
        if node.type == "if":
           
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
            if iterableNode.value == "range":
                result = self.evaluateFunctionCall(iterableNode) #execute the range function
                iterable = result[1] #the tuple returned from range
                currentElementType = "Number" #each of the range elements is a number

            # ALSO CHECK FOR A TUPLE/ARRAY LITERAL/IDENTIFIER
            
            self.vars[key]= Variable(key, None, None)
            for i in iterable:
                self.vars[key].value = i
                self.vars[key].type = currentElementType
                self.evaluate(bodyNode)
            del self.vars[key] #kill the key variable at the end of the scope



        # function definition



        # function call - allowed only after being defined, for built in functions they are allowed all the time
        if node.type == "functionCall":
            self.evaluateFunctionCall(node)

        # method call





    def evaluate(self, ast):
        """
        evaluate and executes the AST 
        """
        for child in ast.children:
            self.evaluateStatement(child)
        return self.vars

# a = Executor.arrayMethods["Array"](1, 2)
# a.append(3)
# print(a)
# print(Executor.arrayMethods)