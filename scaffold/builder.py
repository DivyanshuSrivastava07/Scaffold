from .models import ParseNode,TreeNode

class Builder:
    def build(self,nodes:list[ParseNode]) -> list[TreeNode]:
        roots: list[TreeNode] = []
        stack: list[TreeNode] = []
        for parsed in nodes:
            current = TreeNode(
                name=parsed.name,
                level=parsed.level,
                is_dir=parsed.is_dir
            )
            while stack and stack[-1].level>=current.level:
                stack.pop()
            if stack:
                stack[-1].add_child(current)
            else:
                roots.append(current)
            stack.append(current)

        return roots