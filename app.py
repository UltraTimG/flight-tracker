from flask import Flask, request, redirect, session, render_template, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'anythingreally'

delete_db = True

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    connection = sqlite3.connect('flight_tracker.db')
    cursor = connection.cursor()
    user = cursor.execute(f'SELECT * FROM user WHERE username = ? AND password = ?', (username, password) )
    user = user.fetchone()
    
    if user is not None:
        print('correct pwd')
        
        return render_template('index.html', msg='Login successful', user=user[1])
    else:
        print('ebu retry')
        return render_template('login.html', msg='Invalid username or password')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    connection = sqlite3.connect('flight_tracker.db')

    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY, username VARCHAR(255), password VARCHAR(225))')

    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute(f'INSERT INTO user (username, password) VALUES ( "{username}", "{password}")')
    connection.commit()


    cursor.execute('SELECT * FROM user')
    data = cursor.fetchall()
    print(data)

    delreq = str(input('Do you want to delete the database (yes or no):'))
    if delreq == 'yes':
        cursor.execute('DELETE FROM user WHERE username = TY')
        connection.commit()
        print('Database deleted')
    if delreq == 'no':
        print ('Database not deleted')

    else:
        print('Invalid input, database not deleted')

    print('flight_tracker.db')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)