from flask import Flask, render_template
from routes import api_blueprint
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.register_blueprint(api_blueprint)

@app.route('/')
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
