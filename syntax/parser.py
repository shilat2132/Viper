from customAST import *


class Parser:
    def __init__(self, tokensMatrix):
        self.tokensMatrix = tokensMatrix
        self.currentLine = 0

    def retrieveToken(self):
        try:
            return self.tokensMatrix[self.currentLine][self.currentIndex]
        except:
            return None

    def nextToken(self, currentToken):
        if currentToken + 1 < len(self.tokensMatrix[self.currentLine]):
            return self.tokensMatrix[self.currentLine][currentToken + 1]
        else:
            self.currentLine = self.currentLine + 1
            if self.currentLine < len(self.tokensMatrix):
                return self.tokensMatrix[self.currentLine][0]
            return None

    def parseExp(self, index):
        # handle expressions with ()
        op1 = self.parseTerm(index)
        index += 1
        operator = self.retrieveToken(index)
        if not operator: return op1  #if there is no more then expression is over
        if operator.type not in ["logical_operator", "operator"]:
            raise SyntaxError(f"error in line {self.currentLine} col {index}, expected operator but got {operator}")
        op2 = self.parseTerm(index)

    def parseTerm(self, index) -> AstNode:
        currentToken = self.retrieveToken(index)
        if not currentToken: return None
        if currentToken.type == 'identifier':
            return AstNode('var', {"value": currentToken.value})
        elif currentToken.type == 'number':
            return AstNode('Number', {"value": currentToken.value})
        elif currentToken.type == 'boolean':
            return AstNode('Boolean', {"value": currentToken.value})
        elif currentToken.type == 'boolean':
            return AstNode('Boolean', {"value": currentToken.value})
        else:
            raise SyntaxError(f"Unexpected token: {currentToken} in line {self.currentLine} col {index}")

    def parseStatement(self):
        parent = self.retrieveToken(self.currentIndex)
        if parent.type == "identifier" and self.nextToken(self.index).type == "assign":
            node = AstNode("assign", None, [AstNode("var", {"value": parent.value})])
            index = index + 2
            source = self.parseExp(index)
            node.addChild(source)
            return node

        if parent.type == "Keyword" and parent.value == "if":
            node = AstNode("if", None)
            self.currentIndex += 1
            condition = self.parseExp(self.currentIndex)
            node.addChild(condition)
            while self.retrieveToken(self.index) != "}":
                n = self.parseStatement()
                self.currentLine += 1
                node.addChild(n)

            return node

        if parent.type == "Keyword" and parent.value == "else":
            node = AstNode("else", None)
            self.currentIndex += 1
            condition = self.parseExp(self.currentIndex)
            node.addChild(condition)
            while self.retrieveToken(self.index) != "}":
                n = self.parseStatement()
                self.currentLine += 1
                node.addChild(n)
            return node

        if parent.type == "Keyword" and parent.value == "while":
            node = AstNode("while", None)
            self.currentIndex += 1
            condition = self.parseExp(self.currentIndex)
            node.addChild(condition)
            self.currentIndex += 1
            n = self.retrieveToken()
            if(n.value != "{"):
            while self.retrieveToken(self.index) != "}":\




            while self.retrieveToken(self.index).value != "}":
                self.parseStatement()


    def parse(self):
        ast = Ast()
        i = 0
        while self.currentLine < len(self.tokensMatrix):
            node = self.parseStatement(i)
            ast.AddNode(node)
            self.currentLine += 1
        print(ast)
