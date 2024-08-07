class AstNode:
    
    def __init__(self, type, attrs=None, children=None, parent=None):
        self.type = type
        self.attrs = attrs if attrs else {}
        self.children = children if children else []
        self.parent = parent
    
    def addChild(self, node):
        self.children.append(node)
    
    def setParent(self, node):
        self.parent = node.parent
    
    def __repr__(self) -> str:
        children ="["
        i= 1
        for c in self.children:
            children += f"{i}. {c}"
            i+=1
        children+="] \n"
        return str(f"type: {self.type}, attrs: {self.attrs}, children: {children}")


class Ast:
    def __init__(self) :
        self.rootNode = AstNode("root")
    
    def createNode(self, type, attrs=None, children=None, parent=None):
        if not parent:
            parent = self.rootNode
        node = AstNode(type, attrs, children, parent)
        node.parent.addChild(node)

    def AddNode(self, node: AstNode):
        if not node.parent:
            node.parent = self.rootNode
        node.parent.addChild(node)
    
    def __repr__(self) -> str:
        return str(self.rootNode)