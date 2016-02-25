from flask import Flask, jsonify, render_template
import psycopg2 as dbapi2

application = Flask(__name__)

db = dbapi2.connect (database="dafambackend", user="bankbantul", password="bankbantul")
cur = db.cursor()

def check_login(username, password):
    query = "select id, nama from pengguna where nama='{}' and sandi='{}'".format(username, password)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

@application.route('/login/<nama>/<sandi>')
def login(nama, sandi):
    hasil = {}
    if check_login(nama,sandi):
        hasil['pesan']='masukan benar'
        hasil['succceded'] = True
    else:
        hasil['pesan']='masukan salah'
        hasil['succceded'] = False
    return jsonify(hasil)

@application.route('/get_users')
def get_users():
    cur.execute ("SELECT id, nama, sandi FROM pengguna");
    rows = cur.fetchall()
    users = []
    for i, row in enumerate(rows):
        users.append({'id': row[0]})
        users.append({'nama': row[1]})
        users.append({'sandi': row[2]})

    return jsonify(data=users)

@application.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    application.run(debug=True)
