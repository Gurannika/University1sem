from flask import Flask, render_template, request, redirect
import psycopg2
conn = psycopg2.connect(dbname="service", user="postgres", password="1234", host="localhost", port="5432")
cursor = conn.cursor()

app=Flask(__name__)

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form.get("login"):
            username = request.form.get('username')  # запрос к данным формы
            password = request.form.get('password')
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)),)
            records = list(cursor.fetchall())
            if len(records) == 0:
                return redirect("/login_error/")
            else:
                return render_template('account.html', full_name=records[0][1])
        elif request.form.get("registration"):
            return redirect("/registration/")

    return render_template('login.html')

@app.route('/login_error/', methods=['GET'])
def login_error():
    return render_template('login_error.html')


@app.route('/registration/', methods=['POST', 'GET'])
def reg():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name.replace(" ","").isalpha():
            return render_template('reg_error.html')
        login_user = request.form.get('login')
        password = request.form.get('password')
        cursor.execute(f"SELECT * FROM service.users WHERE login='{str(login_user)}'")
        account = list(cursor.fetchall())
        if not account:
            cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                           (str(name), str(login_user), str(password)))
            conn.commit()

            return redirect('/login/')

        else:
            return render_template('reg_error.html')
    else:
        return render_template('registration.html')
















