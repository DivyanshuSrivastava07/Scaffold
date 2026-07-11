from pathlib import Path
from .models import TreeNode
class FileSystemWriter:
    """
        Writes a TreeNode hierarchy to the filesystem.
    """
    def write(
            self,
            roots:list[TreeNode],
            destination:str|Path,
        ) -> None:
        """
            Create directories and files under the given destination.
        """
        destination = Path(destination)
        for root_node in roots:
            self._write_node(root_node,destination)

    def _write_node(
            self,
            node:TreeNode,
            current_path : Path,
    ) -> None:
        node_path = current_path / node.name
        if not node.is_dir:
            node_path.touch(exist_ok=True)
            return
    
        node_path.mkdir(
            parents=True,
            exist_ok=True
        )
        for child in node.children:
            self._write_node(child,node_path)
        