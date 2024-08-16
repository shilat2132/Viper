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
        """
        the level of the node in the tree - helps with printing the tree in the structure of tree
        """
        self.level = newLevel

    def update_descendant_levels(node):
        """Recursively update the level of all descendants."""
        for child in node.children:
            child.setLevel(node.level + 1)
            AstNode.update_descendant_levels(child)

    def addChild(self, node):
        """
        adds 'node' as a child to the current node and update its level and its descendant's
        """
        node.setParent(self)
        node.setLevel(self.level+1)
        self.children.append(node)
        AstNode.update_descendant_levels(node)
    

    
    def __repr__(self) -> str:
        """
        prints the node in a structure of a tree
        """
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
        """
        initialize the ast with a node of root representing the main program
        """
        self.rootNode = AstNode("root")

    def AddNode(self, node: AstNode):
        """
        if 'node' doesn't have a parent, set its parent to be the root.
        adds the node as a child to its parent's node
        """
        if not node.parent:
            node.parent = self.rootNode
        node.parent.addChild(node)
    
    def __repr__(self) -> str:
        return str(self.rootNode)