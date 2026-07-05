from parser import Parser
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
pars = Parser()
out = pars.parse(text)