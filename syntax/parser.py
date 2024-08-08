import sys
import os
from customAST import *
from utils import *
original_sys_path = sys.path.copy()



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
            Token: returns the current token or None if reached the end of line
        """
        try:
            t = self.tokensMatrix[self.currentLine][self.currentIndex]
            self.currentIndex+=1
            return t
        except:
            return None

    def peekToken(self):
        """
        returns the current token without forwarding the position in the tokens matrix
        Parameters:
        None
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
        funcNode = AstNode("functionCall", {"val": funcName})
        args = self.consumeToken()
        args = argsToList(args.value)
        for arg in args:
            argNode = self.parseTerm(tokenizeLiteralAndIdentifier(arg))
            funcNode.addChild(argNode)
        return funcNode

    def parseExp(self)->AstNode:
        currentToken = self.consumeToken()
        if currentToken:
            if currentToken.type =="openParen":
                op1 = self.parseExp()
            else:
                op1 = self.parseTerm(currentToken) 
        else: return None #if currentToken is None then we reached the end of the line
         
        operator = self.consumeToken()
        if operator and operator.type == "closeParen":
            return op1

        if not operator: return op1 #if there is no more then expression is over

        if operator.type not in ["logical_operator", "operator"]: 
            raise SyntaxError(f"error in line {self.currentLine} col {self.currentIndex}, expected operator but got {operator}")
        op2 = self.parseExp()

        expType = "arithmeticExp" if operator.type == "operator" else "logicalExp"
        return AstNode(expType, {"operator": operator.value}, [op1, op2])
    
    def parseTerm(self, currentToken)->AstNode:
        """
        expects to recieve an identifier or a literal, raise an error if not
        Params: current token
        Returns:
        an ast node of the term, it won;t have children
        """
        if not currentToken: return None
        if currentToken.type == 'identifier':
            return AstNode('var', {"value": currentToken.value})
        elif currentToken.type == 'number':
            return AstNode('Number', {"value": currentToken.value})
        elif currentToken.type == 'boolean':
            return AstNode('boolean', {"value": currentToken.value})
        elif currentToken.type == 'string':
            return AstNode('string', {"value": currentToken.value})
        elif currentToken.type == 'array':
            return AstNode('array', {"value": currentToken.value})
        elif currentToken.type == 'tuple':
            return AstNode('tuple', {"value": currentToken.value})
        else:
            raise SyntaxError(f"Unexpected token: {currentToken} in line {self.currentLine} col {self.currentIndex}")

 
    
    def parseStatement(self):
        parent = self.consumeToken()
        peekToken = self.peekToken()
        if peekToken ==-1:
            return False
        # assign
        if parent.type == "identifier" and peekToken.type == "assign":
            node = AstNode("assign", None, [AstNode("var", {"value": parent.value})])
            self.consumeToken() #forward the position from the assign token
            source = self.parseExp()
            node.addChild(source)
            return node
        
        # function call
        if parent.type=="identifier" and peekToken.type == "tuple":
            return self.parseFunctionCall(parent.value)
        
        # return statement
        if parent.type == "keyword" and parent.value == "return":
            returnStatementNode = AstNode("returnStatement")
            returnValueNode = self.parseExp()
            if returnValueNode != None:
                returnStatementNode.addChild(returnValueNode)
            return returnStatementNode

        if parent.type == "keyword" and parent.value == "if":
            node = AstNode("if", None)
            self.currentIndex += 1
            condition = self.parseExp()
            node.addChild(condition)
            while self.consumeToken().type != "scopeCloseParen":
                n = self.parseStatement()
                self.currentLine += 1
                node.addChild(n)

            return node

        if parent.type == "keyword" and parent.value == "else":
            node = AstNode("else", None)
            self.currentIndex += 1
            condition = self.parseExp(self.currentIndex)
            node.addChild(condition)
            while self.consumeToken().type != "scopeCloseParen":
                n = self.parseStatement()
                self.currentLine += 1
                node.addChild(n)
            return node

        if parent.type == "keyword" and parent.value == "while":
            node = AstNode("while", None)
            self.currentIndex += 1
            condition = self.parseExp(self.currentIndex)
            node.addChild(condition)
            self.currentIndex += 1
            n = self.consumeToken()
            if(n.value != "{"):
                while self.consumeToken().type != "scopeCloseParen":
                    print("d")




            while self.consumeToken(self.index).value != "}":
                self.parseStatement()


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

