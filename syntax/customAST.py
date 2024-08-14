class AstNode:
    
    def __init__(self, type, value=None, children=None, level=0, parent=None):
        self.type = type
        self.value = value
        self.children = children if children else []
        
        self.level = parent.level+1 if parent else level
        self.parent = parent
        # for all children set their parent to be current node
        if children:
            for c in children:
                c.setParent(self)
                c.setLevel(level+1)
    
    def setParent(self, node):
        self.parent = node

    def setLevel(self, newLevel: int):
        self.level = newLevel

    def update_descendant_levels(node):
        """Recursively update the level of all descendants."""
        for child in node.children:
            child.setLevel(node.level + 1)
            AstNode.update_descendant_levels(child)

    def addChild(self, node):
        node.setParent(self)
        node.setLevel(self.level+1)
        self.children.append(node)
        AstNode.update_descendant_levels(node)
    
    def isLeaf(self)-> bool:
        return len(self.children)==0
    

    
    def __repr__(self) -> str:
        return self._repr_helper(self.level, '', False)

    def _repr_helper(self, level: int, prefix: str, is_last: bool) -> str:
        """Helper method to format the AST."""
        indent = '  ' * level
        connector = '└── ' if is_last else '├── '
        repr_str = f"{prefix}{indent}{connector}{self.type}: {self.value}\n"
        
        # New prefix to maintain proper line connections
        new_prefix = prefix + ('    ' if is_last else '│   ')
        
        # Recursively handle children
        for idx, child in enumerate(self.children):
            is_last_child = idx == len(self.children) - 1
            repr_str += child._repr_helper(level + 1, new_prefix, is_last_child)
        
        return repr_str


class Ast:
    def __init__(self) :
        self.rootNode = AstNode("root")
    
    def createNode(self, type, value=None, children=None, parent=None):
        if not parent:
            parent = self.rootNode
        node = AstNode(type, value, children, parent)
        node.parent.addChild(node)

    def AddNode(self, node: AstNode):
        if not node.parent:
            node.parent = self.rootNode
        node.parent.addChild(node)
    
    def __repr__(self) -> str:
        return str(self.rootNode)