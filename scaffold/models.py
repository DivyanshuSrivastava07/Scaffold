from dataclasses import dataclass,field
from typing import Optional
@dataclass(slots=True)
class ParseNode:
    """
        Represents a single parsed line from the input
    """
    name: str
    level: int
    is_dir: bool
@dataclass(slots=True)
class TreeNode:
    """
        Represents the node in the directory tree
    """
    name: str
    level: int
    is_dir:bool
    parent: Optional["TreeNode"] = None
    children:list["TreeNode"] = field(default_factory=list)
    def add_child(self,child:"TreeNode")->None:
        child.parent = self
        self.children.append(child)
    @property
    def is_leaf(self) -> bool:
        return (len(self.child) == 0)