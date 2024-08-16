from typing import Tuple
from customAST import *
from utils import argsToList, checkParenthasesValidation, tokenizeLiteralAndIdentifier



class Parser:
    operatorsDict = {
        "<=": "lessEquals",
        "<": "less",
        ">=": "greaterEquals",
        ">": "greater" ,
        "==": "equal" ,
        "!=": "not_equal",
        "&&": "And",
        "||": "Or",
        "!": "negate",
        "+": "add",
        "-": "sub",
        "*": "mul",
        "/": "div",
        "^": "pow"
    }
    def __init__(self, tokensMatrix):
        self.tokensMatrix = tokensMatrix
        self.currentLine = 0
        self.currentIndex =0


    def nextLine(self):
        """
        forwards position to first token of next line if exists, in the token matrix list
        Parameters:
        None
        Returns:
        bool: return True if forwarding was successful, and False if we reaches the end of the list
        """
        if self.currentLine +1 < len(self.tokensMatrix):
            self.currentLine+=1
            self.currentIndex=0
            return True
        else:
            return False
        
    def consumeToken(self):
        """
           returns the current token in line and forwarding position
            Parameters:
            None
            Returns:
            returns the current token or None if reached the end of line
        """
        try:
            t = self.tokensMatrix[self.currentLine][self.currentIndex]
            self.currentIndex+=1
            return t
        except:
            return None

    def peekToken(self):
        """
        returns the current token without forwarding the position in the tokens matrix, 
        would go to next line if current line is over
        Returns:
        if reached end of code returns -1
        """
        # checks if the next token is within the same line
        if self.currentIndex < len(self.tokensMatrix[self.currentLine]):
            return self.tokensMatrix[self.currentLine][self.currentIndex]
        elif self.currentLine + 1 < len(self.tokensMatrix):
                return self.tokensMatrix[self.currentLine+1][0]
        return -1

    def parseFunctionCall(self, name, isMethod = False, obj = None)->AstNode:
        """
        creating a node of a functionCall/methodCall with the name as value and its 
        args as node with children. if it's a method, add a node for the object
        Params:
        name - the name of the function/method being called
        isMethod - is that a method call or a function call
        obj - if it's a method, that would be the object the method is performed on
        Returns:
        the functionCall node
        """
        mainNode = AstNode("functionCall" if not isMethod else "methodCall", name)
        if isMethod:
            mainNode.addChild(AstNode("var", obj.value))
        self.parseArgsOrValues(mainNode)
        return mainNode

    def parseArgsOrValues(self, mainNode: AstNode, isDef = False, nodeName = "args"):
        """
        for args: creates a node for each argument and adds it to the args node of the mainNode
            
        for values: fits for tuples/arrays literals in which it creates a node of values
                    
            Params: 
                mainNode- the main node of the function
                isDef- are the args of a function/method call or a definition

        """
        argsNode = AstNode(nodeName) #values/args node
        mainNode.addChild(argsNode) 
        
        # consume the token of args represented by a string in a format of tuple, converts it to a list of args
        args = self.consumeToken()
        if not args:
            raise SyntaxError(f"the method/ function {mainNode.value} needs to be called with ()")
        if len(args.value)>2:
            args = argsToList(args.value)

            # for each parameter, tokenize it and adds it as a child node to the args node
            for arg in args:
                argNode = self.parseTerm(tokenizeLiteralAndIdentifier(arg, isDef))
                argsNode.addChild(argNode)


    def parseExp(self, parenthesesAmount=0)->Tuple[AstNode, int] | None:
        """
        creates a subTree recursively for expression: either arithmetical or logical
        Returns: 
        the subtree and the number of parenthases after incrementing if met with ( and decrementing if met with )
        helps for checking parenthases syntax
        """
        currentToken = self.consumeToken()
        if currentToken:
            if currentToken.type =="openParen":
                op1, parenthesesAmount = self.parseExp(parenthesesAmount+1)
            elif currentToken.type =="logical_operator" and currentToken.value =="!":
                negationExp, parenthesesAmount = self.parseExp(parenthesesAmount)
                return AstNode("logicalExp", Parser.operatorsDict["!"], [negationExp]), parenthesesAmount
            else:
                op1 = self.parseTerm(currentToken)
        # expressions must have at least 1 operand
        else: raise SyntaxError(f"syntax Error in line {self.currentLine}")
         
        operator = self.consumeToken()
        if operator and operator.type == "closeParen":
            return op1, parenthesesAmount-1

        if not operator: return op1, parenthesesAmount #if there is no more then expression is over
        if operator.type == "scopeOpenParen" or operator.type == "scopeCloseParen":
            self.currentIndex-=1
            return op1, parenthesesAmount
        if operator.type not in ["logical_operator", "operator"]: 
            raise SyntaxError(f"error in line {self.currentLine} col {self.currentIndex}, expected operator but got '{operator.value}'")
        op2, parenthesesAmount = self.parseExp(parenthesesAmount)

      
        expType = "arithmeticExp" if operator.type == "operator" else "logicalExp"
        return AstNode(expType, Parser.operatorsDict[operator.value], [op1, op2]), parenthesesAmount
    
    def parseTerm(self, currentToken)->AstNode:
        """
        expects to recieve an identifier, literal, method call or a function call, raise an error if not
        Params: current token
        Returns:
        an ast node of the term
        """
        if not currentToken: return None
        # checks if the term is a function call
        if (currentToken.type=="identifier" or currentToken.type=="builtinFunc"):
            # call must be following the function name on the same line, so consuming the 
                # token but then move position backwards in case it's not really a function call
            nextToken = self.consumeToken()
            
            if nextToken:
                self.currentIndex -=1
                if nextToken.type == "tuple":
                    return self.parseFunctionCall(currentToken.value)
           

        if currentToken.type =="identifier":
            nextToken = self.consumeToken()
            
            if nextToken:
                self.currentIndex -=1
                if nextToken.type in ["stringMethod", "arrayMethod", "tupleMethod"]:
                    methodName = self.consumeToken().value
                    return self.parseFunctionCall(methodName, True, currentToken)
        
        if currentToken.type == 'identifier':
                return AstNode('var', currentToken.value)
        
        elif currentToken.type == 'number':
            return AstNode('Number', currentToken.value)
        elif currentToken.type == 'boolean':
            return AstNode('boolean', currentToken.value)
        elif currentToken.type == 'string':
            return AstNode('string', currentToken.value)
        elif currentToken.type == 'array':
            self.currentIndex-=1
            arrayNode = AstNode('Array', currentToken.value)
            self.parseArgsOrValues(arrayNode, False, "values")
            return arrayNode
        elif currentToken.type == 'tuple':
            self.currentIndex-=1
            tupleNode = AstNode('Tuple', currentToken.value)
            self.parseArgsOrValues(tupleNode, False, "values")
            return tupleNode
        else:
            raise SyntaxError(f"Unexpected token: '{currentToken.value}' in line {self.currentLine} col {self.currentIndex-1}")

    def parseBlock(self, parentNode, curlyBracesAmount):
        """
        ensures that each scope is wrapped with {}
        raise an error if body's missing or {} missing

        creates a node representing a scope body with parsed statements and adds it to the parentNode
        
        Params:
        parentNode - the node to add the body node to
        curlyBracesAmount - the current amount of curly braces, used to compare between amount of { and }

        Returns: curlyBracesAmount
        """
        bodyBlockNode = AstNode("body")
        nextToken=self.consumeToken()
        if not nextToken:
            if not self.nextLine(): #if former line finished and so is the code, then syntax error
                raise SyntaxError(f"Missing body of a scope")
            nextToken = self.consumeToken()  # if we moved to next line but code isn't finished
       
        if nextToken.type != "scopeOpenParen":
            raise SyntaxError(f"scopes must have opening parentheses, line {self.currentLine}")
        curlyBracesAmount+=1 #if we got here it means we have {

        endCode = False
        nextToken = self.peekToken()
        # reached end of code with no '}'
        if nextToken==-1:
            raise SyntaxError("Missing '}'")
        isNotCloseParenth = nextToken.type != "scopeCloseParen"

        if not self.consumeToken(): #if reached the end of the line move to next one
            endCode = not self.nextLine()
        else: self.currentIndex-=1 #if we didn't finish the line, go back to the token we consumed
        # iterate as long as we didn't reach end of code or a '}'
        while not endCode and isNotCloseParenth:
            blockStatement, curlyBracesAmount = self.parseStatement(curlyBracesAmount, True)
            bodyBlockNode.addChild(blockStatement)
            isNotCloseParenth = self.peekToken().type != "scopeCloseParen"
            endCode = not self.nextLine()

        if isNotCloseParenth: 
            raise SyntaxError("Missing '}'")
        self.consumeToken() #if we reached here it means we are on the } and need to consume it
        curlyBracesAmount -=1
        if len(bodyBlockNode.children)==0:
            raise SyntaxError(f"Missing body of a scope")
        parentNode.addChild(bodyBlockNode)
        return curlyBracesAmount
    
    def parseStatement(self, curlyBracesAmount = 0, nestedBlock = False)-> Tuple[AstNode, int]:
        """
        parses the current statement, checks for syntax errors
        Params: 
        curlyBracesAmount - the current amount of curly braces(incremented when '{' and decrementing when '}')
        nestedBlock - boolean, True if statement is inside a scope
        Returns: 
        a tuple: first element is AstNode representing the statement, second element is the current amount of curly braces
        """
        node = None
        parent = self.consumeToken()
        nextToken = self.peekToken()

        if nextToken ==-1: #prevents having a line with only one element because it's meanningless
            raise SyntaxError(f"Unresolved statement in line {self.currentLine-1}")
        
        # assign - creates a node of 2 children - target and source, source could be either a term or expression
        if parent.type == "identifier" and nextToken.type == "assign":
            node = AstNode("assign", None, [AstNode("var", parent.value)])
            self.consumeToken() #forward the position from the assign token
            source, parenthasesAmount = self.parseExp()
            checkParenthasesValidation(parenthasesAmount) 
            node.addChild(source)
            
        
        # function call - built in like min(x,y) or custom like fun(1, "2")
        if (parent.type=="identifier" or parent.type=="builtinFunc") and nextToken.type == "tuple":
            node = self.parseFunctionCall(parent.value)
            
        
         # method call - a.append(args)
        if parent.type =="identifier" and nextToken.type in ["stringMethod", "arrayMethod", "tupleMethod"]:
            methodName = self.consumeToken().value
            node = self.parseFunctionCall(methodName, True, parent)
        
        # return statement
        if parent.type == "keyword" and parent.value == "return":
            returnStatementNode = AstNode("return")
            if nextToken.value=="null":
                returnStatementNode.addChild(AstNode("returnValue", "null"))
                node= returnStatementNode
            else: 
                returnValueNode, parenthasesAmount = self.parseExp()
                checkParenthasesValidation(parenthasesAmount)
                if returnValueNode != None:
                    returnStatementNode.addChild(returnValueNode)
                node = returnStatementNode

        # if statement and while loop
        if parent.type == "keyword" and (parent.value == "if" or parent.value == "while"):
            parentNode = AstNode(parent.value)

            # condition
            condition, parenthasesAmount = self.parseExp()
            checkParenthasesValidation(parenthasesAmount)
            if not condition:
                raise SyntaxError(f"Missing condition in line {self.currentLine}")
            parentNode.addChild(condition)
            # block of statements
            curlyBracesAmount = self.parseBlock(parentNode, curlyBracesAmount)

            # check for an else block
            if parent.value == "if":
                nextToken = self.peekToken()
                if nextToken!=-1 and nextToken.value=="else":
                    if not self.consumeToken(): #if we got to end of line, move to next one
                        self.nextLine()
                        self.consumeToken() #consume the else
                    elseNode = AstNode("elseBlock")
                    curlyBracesAmount = self.parseBlock(elseNode, curlyBracesAmount)
                    parentNode.addChild(elseNode)
            
            node = parentNode
            
        # for loop
        if parent.value=="for":
            forNode = AstNode("for")

            # child - iteration variable
            iterationVar = self.consumeToken()
            if not iterationVar or iterationVar.type != "identifier":
                raise SyntaxError(f"line {self.currentLine}: a for loop must have a key to iterate with")
            forNode.addChild(AstNode("iterationVar", iterationVar.value))

            # checks if 'in' exists
            inToken = self.consumeToken()
            if not inToken or inToken.value != "in":
                raise SyntaxError(f"Unexpected token. expected 'in'" )
            
            # check for iterable - still not checking type
            iterable = self.consumeToken()
            if not iterable or (iterable.type not in ["array", "tuple", "identifier"] 
                                and iterable.value != "range"):
                raise SyntaxError(f"line {self.currentLine}: expected iterable object")
            if iterable.value=="range":
                rangeArgs = self.consumeToken()
                if not rangeArgs or rangeArgs.type != 'tuple':
                    raise SyntaxError("not executing range correctly")
                iterableNode = AstNode("functionCall", "range")
                self.currentIndex-=1
                self.parseArgsOrValues(iterableNode)
                forNode.addChild(iterableNode)

            
            elif iterable.type in ["array", "tuple"]:
                name = "Array" if iterable.type =="array" else "Tuple"
                objectNode = AstNode(name, iterable.value)
                self.currentIndex-=1 #to pose back at the tuple/array literal
                self.parseArgsOrValues(objectNode, False, "values")
                forNode.addChild(objectNode)
            else: forNode.addChild(AstNode(iterable.type, iterable.value)) #for identifier

            curlyBracesAmount = self.parseBlock(forNode, curlyBracesAmount)
            # checkParenthasesValidation(curlyBracesAmount, "{}")
            node = forNode
        
        # function definition - function funcName(args){statements}
        if parent.value=="function" and nextToken.type == "identifier":
            node = AstNode("functionDef", nextToken.value)
            self.consumeToken() #consumes the function name
            self.parseArgsOrValues(node, True)
            curlyBracesAmount = self.parseBlock(node, curlyBracesAmount)
            # checkParenthasesValidation(curlyBracesAmount, "{}")

        if node:
            next = self.consumeToken()
            while next and next.value in ["{", "}"]:
                if next.value == "{": curlyBracesAmount +=1
                else: curlyBracesAmount -=1
                next = self.consumeToken()
            # i wanna check curly braces validation only in the outer block
            if not nestedBlock: 
                checkParenthasesValidation(curlyBracesAmount, "{}")
            return node, curlyBracesAmount
        
        raise SyntaxError(f"line {self.currentLine}: illegal statement")


    def parse(self):
        """
        creates Ast with one root of the main program
        """
        ast = Ast()
        endOfCode = False
        while not endOfCode:
            node, curlyBracesAmount = self.parseStatement()
            if not node: break
            ast.AddNode(node)
            endOfCode = not self.nextLine()
        print(ast)
        return ast

