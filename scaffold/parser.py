from .models import ParseNode
class Parser:
    """
        Convert the indented directory description into ParseNode Objects.
    """
    def parse(self,text:str)->list[ParseNode]:
        """
            Parse the give text into parse nodes and reture parsenode objects.
        """
        nodes = []
        for line in self._clean_lines(text):
            node = ParseNode(
                self._extract_name(line),
                self._indent(line),
                self._is_directory(line)
               )
            nodes.append(node)
        return nodes
    def _clean_lines(self,text:str)->list[str]:
        """
            Remove blank lines and trailing whitespaces.
        """
        lines = []
        for line in text.splitlines():
            line = line.rstrip()
            if line:
                lines.append(line)
        return lines
    def _indent(self,line:str) -> int:
        """
        count leading spaces.
        """
        return len(line) - len(line.lstrip())
    def _is_directory(self,line:str)->  bool:
        """
        Determines whether the line 
        represent the directory.
        """
        return line.strip().endswith('/')
    def _extract_name(self,line:str) -> str:
        """
        Remove indentation and trailing slash.
        """
        return line.strip().rstrip('/')
    

