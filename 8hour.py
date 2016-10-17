from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL
from secret import Secret

mysql =  MySQL()
app = Flask(__name__)

Secret = Secret()

app.config['MYSQL_DATABASE_USER'] = Secret.user
app.config['MYSQL_DATABASE_PASSWORD'] = Secret.pw
app.config['MYSQL_DATABASE_DB'] = Secret.db
app.config['MYSQL_DATABASE_HOST'] = Secret.host
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

cursor.execute("SELECT T1.item_id, GROUP_CONCAT(T1.meta_value SEPARATOR ', ') AS Result FROM wp_kczafk_frm_item_metas T1 GROUP BY T1.item_id")
result = cursor.fetchall()


for i in range (0, len(result)):
    table_list = result[i][1].split(', ', 5)
    for j in range (0, len(table_list)):
        if table_list[j] is None:
            table_list[j] = 'NULL'
    if len(table_list) < 3:
        print "This Person Sucks Hambone"
    elif len(table_list) < 6:
        cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], 'NULL', 'NULL', 'NULL'))
    elif len(table_list) == 6:
        cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], table_list[3], table_list[4], table_list[5]))
    conn.commit()
    cursor.execute("INSERT INTO just_email_list VALUES (%s)", table_list[2])
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True)

