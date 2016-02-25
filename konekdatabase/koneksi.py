import psycopg2 as dbapi2


db = dbapi2.connect (database="dafambackend", user="bankbantul", password="bankbantul")
cur = db.cursor()

#clear data
cur.execute ("DELETE FROM pengguna")

#insert data
insert = "insert into pengguna(id, nama, sandi) values('{}','{}','{}')"
cur.execute(insert.format('123','atiq', 'jugarahasia'))
cur.execute(insert.format('456','yaslam', 'rahasia'))

cur.execute ("SELECT * FROM pengguna");
rows = cur.fetchall()
for i, row in enumerate(rows):
    print("Row", i, "value = ", row)

db.commit()
cur.close()
db.close()


def check_login(username, password):
    query = "select id, nama from pengguna where nama='{}' and sandi='{}'".format(username, password)
    cur.execute(query)
    rows = cur.fetchall()
    return len(rows) > 0

db = dbapi2.connect (database="dafambackend", user="bankbantul", password="bankbantul")
cur = db.cursor()

# selanjutnya pergunakan fungsi check_login tersebut
print(check_login('yaslam', 'rahasia'))