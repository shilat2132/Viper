from typing import Tuple
from customAST import *
from utils import *



class Parser:
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

    def parseFunctionCall(self, funcName)->AstNode:
        """
        creating a node of a functionCall with the funcName and its args as children
        Params:
        funcName - the name of the function being called
        Returns:
        the functionCall node
        """
        funcNode = AstNode("functionCall", funcName)
        args = self.consumeToken()
        args = argsToList(args.value) # type: ignore
        for arg in args:
            argNode = self.parseTerm(tokenizeLiteralAndIdentifier(arg)) # type: ignore
            funcNode.addChild(argNode)
        return funcNode

    def parseExp(self, parenthesesAmount=0)->Tuple[AstNode, int] | None:
        """
        creates a subTree recursively for expression: either arithmetical or logical
        """
        currentToken = self.consumeToken()
        if currentToken:
            if currentToken.type =="openParen":
                op1, parenthesesAmount = self.parseExp(parenthesesAmount+1)
            elif currentToken.type =="logical_operator" and currentToken.value =="!":
                negationExp, parenthesesAmount = self.parseExp(parenthesesAmount)
                return AstNode("logicalExp", "!", [negationExp]), parenthesesAmount
            else:
                op1 = self.parseTerm(currentToken) 
        else: return None #if currentToken is None then we reached the end of the line
         
        operator = self.consumeToken()
        if operator and operator.type == "closeParen":
            return op1, parenthesesAmount-1

        if not operator: return op1, parenthesesAmount #if there is no more then expression is over
        if operator.type == "scopeOpenParen" or operator.type == "scopeCloseParen":
            self.currentIndex-=1
            return op1, parenthesesAmount
        if operator.type not in ["logical_operator", "operator"]: 
            raise SyntaxError(f"error in line {self.currentLine} col {self.currentIndex}, expected operator but got {operator.type} of '{operator.value}'")
        op2, parenthesesAmount = self.parseExp(parenthesesAmount)

      
        expType = "arithmeticExp" if operator.type == "operator" else "logicalExp"
        return AstNode(expType, operator.value, [op1, op2]), parenthesesAmount
    
    def parseTerm(self, currentToken)->AstNode:
        """
        expects to recieve an identifier or a literal, raise an error if not
        Params: current token
        Returns:
        an ast node of the term, it won;t have children
        """
        if not currentToken: return None
        if currentToken.type == 'identifier':
            return AstNode('var', currentToken.value)
        elif currentToken.type == 'number':
            return AstNode('Number', currentToken.value)
        elif currentToken.type == 'boolean':
            return AstNode('boolean', currentToken.value)
        elif currentToken.type == 'string':
            return AstNode('string', currentToken.value)
        elif currentToken.type == 'array':
            return AstNode('array', currentToken.value)
        elif currentToken.type == 'tuple':
            return AstNode('tuple', currentToken.value)
        else:
            raise SyntaxError(f"Unexpected token: '{currentToken.value}' in line {self.currentLine} col {self.currentIndex-1}")

    def parseBlock(self, parentNode):
        nextToken=self.consumeToken()
        if not nextToken:
            if not self.nextLine(): #if former line finished and so is the code, then syntax error
                raise SyntaxError(f"Missing body in line {self.currentLine-1}")
            nextToken = self.consumeToken()
        # if we moved to next line but code isn't finished
        if nextToken.type != "scopeOpenParen":
            raise SyntaxError(f"scopes must have opening parentheses, line {self.currentLine}")
        endCode = False
        isNotCloseParenth = self.peekToken().type != "scopeCloseParen"
        if not self.consumeToken(): #if reached the end of the line move to next one
            endCode = not self.nextLine()
        else: self.currentIndex-=1 #if we didn't finish the line, go back to the token we consumed
        while not endCode and isNotCloseParenth:
            blockStatement = self.parseStatement()
            parentNode.addChild(blockStatement)
            isNotCloseParenth = self.peekToken().type != "scopeCloseParen"
            endCode = not self.nextLine()

        if isNotCloseParenth: 
            raise SyntaxError("Missing '}'")
        self.consumeToken() #if we reached here it means we are on the } and need to consume it
 
    
    def parseStatement(self):
        parent = self.consumeToken()
        nextToken = self.peekToken()
        if nextToken ==-1:
            raise SyntaxError(f"Unresolved statement in line {self.currentLine-1}")
        # assign
        if parent.type == "identifier" and nextToken.type == "assign":
            node = AstNode("assign", None, [AstNode("var", parent.value)])
            self.consumeToken() #forward the position from the assign token
            source, parenthasesAmount = self.parseExp()
            checkParenthasesValidation(self.currentLine, parenthasesAmount) # type: ignore
            node.addChild(source)
            return node
        
        # function call - keyword is for build in functions such as print and range
        if (parent.type=="identifier" or parent.type=="keyword") and nextToken.type == "tuple":
            return self.parseFunctionCall(parent.value)
        
        # return statement
        if parent.type == "keyword" and parent.value == "return":
            returnStatementNode = AstNode("returnStatement")
            returnValueNode, parenthasesAmount = self.parseExp()
            checkParenthasesValidation(self.currentLine, parenthasesAmount) # type: ignore
            if returnValueNode != None:
                returnStatementNode.addChild(returnValueNode)
            return returnStatementNode

        # if statement and while loop
        if parent.type == "keyword" and (parent.value == "if" or parent.value == "while"):
            parentNode = AstNode(parent.value)

            # condition
            condition, parenthasesAmount = self.parseExp()
            checkParenthasesValidation(self.currentLine, parenthasesAmount) # type: ignore
            if not condition:
                raise SyntaxError(f"Missing condition in line {self.currentLine}")
            parentNode.addChild(condition)
            # block of statements
            self.parseBlock(parentNode)

            # check for an else block
            if parent.value == "if":
                nextToken = self.peekToken()
                if nextToken!=-1 and nextToken.value=="else":
                    if not self.consumeToken(): #if we got to end of line, move to next one
                        self.nextLine()
                        self.consumeToken() #consume the else
                    elseNode = AstNode("elseBlock")
                    self.parseBlock(elseNode)
                    parentNode.addChild(elseNode)
            return parentNode
            
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
            if not iterable or (iterable.type != "identifier" 
                                and iterable.type not in ["array", "tuple"] 
                                and iterable.value != "range"):
                raise SyntaxError(f"line {self.currentLine}: expected iterable object")
            if iterable.value=="range":
                rangeArgs = self.consumeToken()
                if not rangeArgs:
                    raise SyntaxError(f"line {self.currentLine}: range function wasn't called but just mentioned")
                forNode.addChild(AstNode(iterable.value, rangeArgs.value ))
            else: forNode.addChild(AstNode(iterable.type, iterable.value))
            self.parseBlock(forNode)
            return forNode


    def parse(self):
        """
        creates Ast with one root of the main program
        """
        ast = Ast()
        endOfCode = False
        while not endOfCode:
            node = self.parseStatement()
            if not node: break
            ast.AddNode(node)
            endOfCode = not self.nextLine()
        print(ast)

