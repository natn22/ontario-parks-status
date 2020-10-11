# from flask import Flask
# import main

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()

from src import create_app

if __name__ == "__main__":
    app = create_app()
    app.run()