"""
Flask main file
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    Hello World example endpoint
    :return:
    """
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
