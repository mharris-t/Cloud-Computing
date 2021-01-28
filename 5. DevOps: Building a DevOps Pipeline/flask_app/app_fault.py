"""[summary]

    Returns:
        [type]: [description]
"""
from flask import Flask

app = Flask(__name__)

# Root
@app.route('/')
def get_route():
    """[summary]

    Returns:
        [type]: [description]
    """
    output = {'message': 'Cloud Software'}
    return output, 202
