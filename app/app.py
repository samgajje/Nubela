"""
This is a simple Flask application that returns 'Hello from DevOps!' on the home route.
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    This function returns the message 'Hello from DevOps!' when the home route is accessed.
    """
    return 'Hello from DevOps!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
