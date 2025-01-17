from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL 
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola mundo'

@app.route('/add_contact')
def add_contact():
    return 'ADD_CONTACT'

@app.route('/edit_contact')
def edit_contact():
    return 'EDIT CONTACT'

@app.route('/update_contact')
def update_contact():
    return 'UPDATE CONTACTO'

@app.route('/delete_contact')
def delete_contact():
    return 'delete_contact'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')