import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug import secure_filename
from main import save_to_file



app = Flask(__name__)
app.secret_key = 'decathlon'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = 'input.csv'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        save_to_file()
        return redirect(url_for('uploaded_file',filename='data.json'))
    else:
        flash("No or wrong file selected! This version of the app only accepts csv's")
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
    )
