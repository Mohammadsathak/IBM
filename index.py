# from wsgiref.simple_server import WSGIServer
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

    # @app.route('/about')
    # def about():
    #     return 'About'

if __name__ == '__main__':
    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="5000")
   