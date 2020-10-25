from flask import Flask
import os
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def hello():

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE increment (d text)''')
    except Exception as e:
        print('DB already created')

    html = "<h3>Hello!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/plus")
def plus():
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    date = datetime.date.today()
    cursor.execute('INSERT INTO increment VALUES ("{date}")')
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM increment')
    html = f"<h3> Page was reloaded {cursor.fetchone()[0]} times </h3>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)