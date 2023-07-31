from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! FLASK_DEV : %s' % os.environ.get('FLASK_DEV', False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')