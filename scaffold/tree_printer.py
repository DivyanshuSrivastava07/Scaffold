from .models import TreeNode

class TreePrinter:
    """
    Renders a TreeNode hierarchy into a printable tree string.
    """

    def render(self, roots: list[TreeNode]) -> str:
        lines: list[str] = []
        for root in roots:
            # Root nodes are printed without connectors
            lines.append(root.name)

            for i, child in enumerate(root.children):
                self._render_node(
                    child,
                    prefix="",
                    is_last=(i == len(root.children) - 1),
                    lines=lines,
                )

        return "\n".join(lines)

    def _render_node(
        self,
        node: TreeNode,
        prefix: str,
        is_last: bool,
        lines: list[str],
    ) -> None:

        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + node.name)
        new_prefix = prefix + ("    " if is_last else "│   ")

        for i, child in enumerate(node.children):
            self._render_node(
                child,
                new_prefix,
                i == len(node.children) - 1,
                lines,
            )