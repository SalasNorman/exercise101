from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('phonebook.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS contacts 
              (pbid INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    with sqlite3.connect('phonebook.db') as conn:
        contacts = conn.execute('''SELECT * FROM contacts''').fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        with sqlite3.connect('phonebook.db') as conn:
          conn.execute('''INSERT INTO contacts (name, phone) VALUES (?, ?)''', (name, phone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:pbid>')
def delete(pbid):
    with sqlite3.connect('phonebook.db') as conn:
        conn.execute('''DELETE FROM contacts WHERE pbid = ?''', (pbid,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:pbid>', methods=['GET', 'POST'])
def edit(pbid):
    with sqlite3.connect('phonebook.db') as conn:
        contact = conn.execute('''SELECT * FROM contacts WHERE pbid = ?''', (pbid,)).fetchone()
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        with sqlite3.connect('phonebook.db') as conn:
            conn.execute('''UPDATE contacts SET name = ?, phone = ? WHERE pbid = ?''', (name, phone, pbid))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit.html', contact=contact)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)