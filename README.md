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
- Standardmäßig antwortet die Flask-Route auf GET-Anforderungen. Sie können diese Einstellung jedoch ändern, indem Sie Methodenparameter für den route()-Decorator bereitstellen.

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
```python
  action="/" method="post" enctype="multipart/form-data"
```
> das ist ein Codierungstyp, mit dem Dateien über einen POST gesendet werden können . Ganz einfach, ohne diese Codierung können die Dateien nicht über POST gesendet werden . 
> >Wenn Sie einem Benutzer erlauben möchten, eine Datei über ein Formular hochzuladen, müssen Sie diesen Enctype verwenden.

22. Zusammenfassend für das uploading mehrerer Dateien sollte unsere <kbd>/</kbd>-Route so aussehen.
```python

  from flask import Flask, request, render_template, redirect, flash
from models import Schema


app = Flask(__name__) #__main__

@app.route("/")
def hellopexonian():
    return "Hello Pexonian, trage hier deine Zertifizierungen ein! "


@app.route('/', methods=["GET", "POST"]) #route for uploading file
def index():
    if request.method == "GET":
        return render_template('index.html')

    if not 'file' in request.files:
        flash('No file part in request')  #No file part in request
        return redirect(request.url)

    files = request.files.getlist('file')  #list for uploading multiple files

    for file in files:
        if file.filename == '':
            flash('No file uploaded')  #No file uploaded'
            return redirect(request.url)
        else:
            flash('File type not supported')
            return redirect(request.url)

    return "Files uploaded successfully"

if __name__ == "__main__":
    Schema()
    app.run(debug = True)

```

```python
 @app.route('/', methods=["GET", "POST"])
```
- GET: ruft daten vom server ab.
- Post: sendet daten an den server zum erstellen einer Neuen Entität. 
- PUT: ähnlich wie post wird aber verwendet um eine vorhandene Entität zu ersetzen.
> By default, the Flask route responds to GET requests.However, you can change this preference by providing method parameters for the route () decorator.

> Um sowohl GET- als auch POST-Anforderungen zu verarbeiten, fügen wir dies in der Methode decoder app.route() hinzu. Was auch immer Sie wünschen, Sie ändern es im decode.

### Connect SQLite database
- SQLite funktioniert gut mit Python, da die Python-Standardbibliothek das sqlite3-Modul bereitstellt, mit dem Sie mit jeder SQLite-Datenbank interagieren können, ohne etwas installieren zu müssen. Die Verwendung von SQLite mit Python erfordert im Vergleich zu anderen Datenbank-Engines auch eine minimale Einrichtung.
  
```python
  import sqlite3  #sqlite importiere

class Schema: #class
    def __init__(self): #init function
        self.conn = sqlite3.connect('Bewerbung') #db datei in sqlite
        self.create_todo_table()   #funktion aufrufen

    def create_todo_table(self): #Function
        query = """
            CREATE TABLE IF NOT EXISTS "Bewerbung" (
                id INTEGER PRIMARY KEY,
                Title TEXT,
                Description TEXT            
            );
        """          #tabelle in sql erstellen

        self.conn.execute(query) #querry ausführen
```
- wir verwenden das sqlite3, um mit der Datenbank zu interagieren, die in der standardmäßigen Python-Bibliothek verfügbar ist.

- Daten in SQLite werden in Tabellen und Spalten gespeichert, daher müssen wir zuerst eine Tabelle namens mit den erforderlichen columns erstellen. Sie erstellen eine sql.file, die SQL commands enthält, um die Beitragstabelle mit einigen columns zu erstellen. Anschließend verwenden wir diese Schemadatei, um die Datenbank zu erstellen.

- In Schema löschen wir zunächst die Posts-Tabelle, falls sie bereits vorhanden ist. Dies vermeidet die Möglichkeit, dass eine weitere Tabelle mit dem Namen posts existiert, was zu verwirrendem Verhalten führen könnte (z. B. wenn sie unterschiedliche Spalten hat).


