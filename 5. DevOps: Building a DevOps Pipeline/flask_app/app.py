"""[summary]

    Returns:
        [type]: [description]
"""
from flask import Flask

app = Flask(__name__)

# Root
@app.route('/')
def get_route():
    output = {'message': 'Cloud Software and Systems'}
    return output, 200
