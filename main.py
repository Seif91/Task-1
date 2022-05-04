from flask import Flask, request, render_template, redirect, flash
from models import Schema


app = Flask(__name__) #__main__

@app.route("/")
def hellopexonian():
    return "Hello Pexonian, trage hier deine Zertifizierungen ein! "


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')

    if not 'file' in request.files:
        flash('No file part in request')
        return redirect(request.url)

    files = request.files.getlist('file')

    for file in files:
        if file.filename == '':
            flash('No file uploaded')
            return redirect(request.url)
        else:
            flash('File type not supported')
            return redirect(request.url)

    return "Files uploaded successfully"

if __name__ == "__main__":
    Schema()
    app.run(debug = True)



