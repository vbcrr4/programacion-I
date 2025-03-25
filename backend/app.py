from flask import Flask
import os

app = Flask(__name__)

def home():
    return "Hello, Flask!"

app.add_url_rule('/', 'home', home)

if __name__ == '__main__':
    port = int(os.getenv('server_port', 5000))
    app.run(debug=True, port=port)