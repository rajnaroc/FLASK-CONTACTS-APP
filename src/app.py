from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
from os import getenv
from flask_mysqldb import MySQL 
load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = getenv('MYSQL_DB')
app.secret_key = getenv('SECRET_KEY')

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s, %s, %s)', (fullname,phone,email))
        
        mysql.connection.commit()
        flash("Contact Added Successfully")

        return redirect(url_for('index'))

@app.route('/edit_contact')
def edit_contact():
    return 'EDIT CONTACT'

@app.route('/update_contact')
def update_contact():
    return 'UPDATE CONTACTO'

@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from contacts where id= %s', (id))
    mysql.connection.commit()
    flash('Conctat Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')