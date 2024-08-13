from vars import Vars, Variable
from dispatch import dispatchBuiltInFunctionsInit, dispatchArrayMethodsInit, dispatchTupleMethodsInit

class Executor:

    builtInFunctions, arrayMethods, tupleMethods = {}, {}, {}
    dispatchBuiltInFunctionsInit(builtInFunctions)
    dispatchArrayMethodsInit(arrayMethods)
    dispatchTupleMethodsInit(tupleMethods)

   
    def __init__(self):
        self.vars = Vars()

# needs to take care of function call and method call later
    def evaluateTerm(self, node):
        """
        evaluates a term which might be: a literal/ a variable/ a function call/ a method call
        Returns: 
        type, value of the term
        """
        returnType, value = None, None

        #literal
        if node.type in ["Number", "boolean", "string"]:
            returnType, value= node.type, node.value
        
        # variable - raises an error if variable doesn't exist
        if node.type == "var":
            var = self.vars[node.value]
            returnType, value = var.type, var.value
        
        return returnType, value
    

    def evaluateExp(self, node):
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
            returnType, value = self.evaluateTerm(node)

        return returnType, value
    
    def evaluateStatement(self, node):
        if node.type == "assign":
            target = node.children[0].value #the name of the target var
            source = self.evaluateExp(node.children[1]) #returns a tuple of type and value
            self.vars[target] = Variable(target, source[0], source[1])


    def evaluate(self, ast):
        for child in ast.children:
            self.evaluateStatement(child)
        print(self.vars)

