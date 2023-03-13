import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "I'm hungry"

@app.route('/tasty')
def image():
    return f'''<h1>Look how tasty it is!</h1><img src="{url_for('static', filename='img/tasty.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)