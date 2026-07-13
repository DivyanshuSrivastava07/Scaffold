from pathlib import Path

from .parser import Parser
from .builder import Builder
from .writer import FileSystemWriter


class Scaffold:
    """
    High-level API for generating project structures.
    """

    def generate(
        self,
        text: str,
        destination: str | Path,
    ) -> None:

        nodes = Parser().parse(text)

        roots = Builder().build(nodes)

        # Validator().validate(roots)

        FileSystemWriter().write(
            roots,
            destination,
        )