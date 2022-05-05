## Task-1: Creation of a Python backend application with Flask

### Overview
Erstellung eine Python Backend Applikation mit Flask. Das Ziel ist, das ein Mitarbeiter bei Pexon alle seine Zertifizierungen in einer kleinen WebApp speichern kann.
dazu wird ein Backend und eine Datenbank heruntergeladen:
- PyCharm Community Edition (Backend)
- SQLite (Data Base) 

| &emsp;&emsp;&emsp;Table of Contents |
| --------------------------- |
| 1. [**Creating the application**](#creating-our-application) |
| 2. [**Uploading files**](#uploading-files) |
| 3. [**Connect SQLite database**](#connect-sqlite-database) |


### Setting up the environment projekt erstellen und Flask installieren
- Flask installieren 
  - wir geben unten in das terminal rein:  
```bash
  > pip install flask
```
- Flask wird installieret (Dauert einen kleinen moment) 

### Note:
> Beim wechseln in die Palmen Konsole bekommen wir pop up von der Windows defender firewall wir lassen den zugriffen. 
> - Flask erstellt im localhost ein server, vielleicht auch nach außen dafür brauchen wir diese firewall ein und ausgänge    

### Step by Step Guide

### Creating our application

1. Flask importieren.
```python
  from flask import Flask, render_template, request, redirect,
```
- Flask: Micro web framework.

- render_template: wird verwendet, um eine Ausgabe aus einer Vorlagendatei basierend auf der Jinja2-Engine zu generieren, die sich im Vorlagenordner der Anwendung befindet.

- request: ermöglicht es, Daten zu erhalten, die vom Client, z.B. einem Webbrowser, gesendet werden, damit Sie die Generierung der Antwort entsprechend haben können.

- redirect: Funktion ermöglicht es uns, einen Benutzer auf die URL unserer Wahl umzuleiten.

-  flash: Methode wird verwendet, um informative Nachrichten in der flask zu erzeugen. Es erstellt eine Nachricht in einer Ansicht und gibt sie an eine als nächstes aufgerufene Vorlagenansichtsfunktion weiter.

2. applikation erstellen 
```python
  app = Flask(__name__)
```
3. localhost starten (Hello World beispiel) 
```python
@app.route("/")
def hellopexonian():
    return "Hello Pexonian, trage hier deine Zertifizierungen ein! "

if __name__ == "__main__":
    app.run(debug = True)
```
- App aktiviert, flask server gestartet.
 - (debug = True)=> debug mode on: beim code_zeilen ändern und speichern lädt die seite automatisch neu.
 
4. Input Feld
```python
  @app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']

        upload = Upload(filename=file.filename, data=file.read())
        return f'Uploaded: {file.filename}'
    return render_template('index.html')
  
```

### Uploading files

wir werden ein <kbd>index.html</kbd> Template verwenden, mit dem wir eine Datei hochladen können.  
```python
  
    return render_template('index.html')
```
1. uploading single file

- <kbd>index.html</kbd> Template

```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Files in Flask</title>
  </head>
  <body>
    <div class="container">
      <h1>Hello Pexonian, trage hier deine Zertifizierungen ein!</h1>
      <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload">
      </form>
    </div>
  </body>
  </html>
```

> Das obige Programm erstellt eine HTML-Datei 
> =>definiert ein Dateiauswahlfeld und eine "Durchsuchen"-Schaltfläche für Datei-Uploads.

22. Zusammenfassend für das uploading mehrerer Dateien sollte unsere <kbd>/</kbd>-Route so aussehen.
```python
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

      if file_valid(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADS_FOLDER'], filename))
      else:
        flash('File type not supported')
        return redirect(request.url)
        
    return "Files uploaded successfully"
```


### Connect SQLite database

23. Now, lets see on how to send files as attachments. Inorder to send files as attachment we will be using <kbd>send_from_directory()</kbd> function in Flask.

24. Whenever the user goes into <kbd>/uploads/images/\<filename></kbd> we want to send the file as a attachment.
```python
  @app.route('/uploads/images/<path:filename>')
  def send_attachment(filename):
    return send_from_directory(app.config['UPLOADS_FOLDER'], 
      filename = filename, as_attachment = True)
```
> - The <kbd>path</kbd> is a URL converter in Flask. Which is used to get the entire path in the URL which comes after /uploads/images/

25. Thats all it takes to send attachments in Flask. We just need the filename and the directory from where we are going to send the file.

- We have come to the end of this episode. Hope you learnt something new. If you have any queries just raise an issue.
- To see the YouTube demonstration of this episode [click here](https://youtu.be/Bj4cjo5R_6s).

[[**Back to top**](#files-in-flask)]

<p align="right">
  <a href="https://github.com/ASHIK11ab/Flask-Series/tree/todo-list-app-part2">
    <strong><--Prev</strong>
  </a>
</p>
<p align="right">
  <a href="https://github.com/ASHIK11ab/Flask-Series/tree/OAuth-implementation">
    <strong>Next--></strong>
  </a>
</p>

