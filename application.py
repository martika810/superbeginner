import os
from flask import Flask, render_template,send_from_directory
from flask_bootstrap import Bootstrap

template_folder = os.path.join(os.path.dirname(__file__),'templates')
static_folder = os.path.join(os.path.dirname(__file__),'static')
app = Flask(__name__, template_folder = template_folder, static_folder=static_folder )

Bootstrap(app)

@app.route('/')
def app_entrypoint():
    return render_template('index.html')

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)

@app.route('/imgs/<path:filename>')
def serve_imgs(filename):
    return send_from_directory('static/imgs', filename)

@app.route('/<path:filename>')
def send_html(filename):
    return render_template(filename)

if __name__ == '__main__':
    app.run(debug=True)