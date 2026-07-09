from parser import Parser
from tree_printer import TreePrinter
from builder import Builder

text = """
backend/

    app/
        main.py

        api/
            auth.py
            users.py
            predict.py

        models/
            user.py
            prediction.py

        schemas/

        services/
            auth.py
            ai.py
            image.py

        database/
            db.py

        middleware/

        utils/

    uploads/

    model/

requirements.txt
"""
nodes = Parser().parse(text)
roots = Builder().build(nodes)

out = TreePrinter().render(roots)
print(out)