# ForgeTree

Stop creating project folders by hand.

ForgeTree converts a simple indented text description into a complete directory structure with a clean, modular architecture.

Example:
```
backend/
    app/
        main.py

    ↓

backend/
└── app/
    └── main.py
```
---

## Why ForgeTree?

While working on experiments and side projects, I found myself repeatedly creating the same directory structures by hand.

ForgeTree was created to solve that problem by converting a simple indented text description into a complete project structure while keeping parsing, tree construction, rendering, and filesystem generation as independent components.

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

Clone the repository:

```bash
git clone https://github.com/DivyanshuSrivastava07/ForgeTree.git
```

Or install locally:

```bash
pip install -e .
```

*(Coming soon)*

```bash
pip install scaffold
```

---

## Usage

## Quick Start

```python
from scaffold import generate

tree = """
backend/
    app/
        main.py

requirements.txt
"""

generate(tree, "project")
```
## Advanced Usage

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
Input Text
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
   ├────────────► TreePrinter
   │
   └────────────► FileSystemWriter
```
---

## Project Structure

```text
scaffold/
│
├── parser.py
├── builder.py
├── facade.py
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
- [ ] CLI
- [ ] File Templates
- [ ] Variable Interpolation
- [ ] PyPI Release

---

## Core Components

- Parser – Converts text into parsed nodes.
- Builder – Builds the tree hierarchy.
- TreePrinter – Renders the tree.
- FileSystemWriter – Writes files and folders.
- generate() – One-line project generation.

---

## Contributing

ForgeTree is actively developed.
Contributions, bug reports, and feature requests are welcome.

---

## License

MIT License