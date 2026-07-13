# Scaffold

A lightweight Python library for generating project directory structures from an indented text description.

Instead of manually creating folders and files, describe your project structure in plain text and let Scaffold build it for you.

---
## why I built it
I built Scaffold while repeatedly creating the same project structures for experiments and side projects. I wanted a lightweight, extensible library that separates parsing, tree construction, rendering, and filesystem generation into independent components.

## Features

- 📁 Parse indented directory structures
- 🌳 Build an in-memory tree representation
- 🖨️ Render the directory tree
- 💾 Generate folders and files on disk
- 🧩 Modular architecture
- 🧪 Easy to test and extend

---

## Example

### Input

```text
backend/
    app/
        main.py

        api/
            auth.py
            users.py

        models/
            user.py

uploads/

requirements.txt
```

### Rendered Tree

```text
backend
└── app
    ├── main.py
    ├── api
    │   ├── auth.py
    │   └── users.py
    └── models
        └── user.py

uploads

requirements.txt
```

### Generated Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── auth.py
│   │   └── users.py
│   └── models/
│       └── user.py
├── uploads/
└── requirements.txt
```

---

## Installation

```bash
pip install scaffold
```

*(Coming soon)*

---

## Usage

```python
from scaffold.parser import Parser
from scaffold.builder import Builder
from scaffold.tree_printer import TreePrinter
from scaffold.writer import FileSystemWriter

text = """
backend/
    app/
        main.py

requirements.txt
"""

parser = Parser()
builder = Builder()
printer = TreePrinter()
writer = FileSystemWriter()

nodes = parser.parse(text)
roots = builder.build(nodes)

print(printer.render(roots))

writer.write(
    roots,
    destination="project",
)
```

---

## Architecture

```
Text
 │
 ▼
Parser
 │
 ▼
ParsedNode
 │
 ▼
Builder
 │
 ▼
TreeNode
 ├──────────────► TreePrinter
 │
 ▼
FileSystemWriter
 │
 ▼
Filesystem
```

---

## Project Structure

```text
scaffold/
│
├── parser.py
├── builder.py
├── tree_printer.py
├── writer.py
├── models.py
└── exceptions.py
```

---

## Roadmap

- [x] Parser
- [x] Tree Builder
- [x] Tree Renderer
- [x] File System Writer
- [ ] Validator
- [ ] CLI
- [ ] File Templates
- [ ] Variable Interpolation
- [ ] PyPI Release

---

## Contributing

Contributions, bug reports, and feature requests are welcome.

---

## License

MIT License