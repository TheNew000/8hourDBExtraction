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


# Second Algorithm checking for duplicate entries:

for i in range (0, len(result)):
    table_list = result[i][1].split(', ', 5)
    for j in range (0, len(table_list)):
        if table_list[j] is None:
            table_list[j] = 'NULL'
    if len(table_list) < 3:
        print "This Person Sucks"
    elif len(table_list) < 6:
        cursor.execute("SELECT Email FROM email_list WHERE Email = %r", table_list[2])
        email_present = cursor.fetchone()
        if email_present is None:
            cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], 'NULL', 'NULL', 'NULL'))
    elif len(table_list) == 6:
        cursor.execute("SELECT Email FROM email_list WHERE Email = %r", table_list[2])
        email_present = cursor.fetchone()
        if email_present is None:
            cursor.execute("INSERT INTO email_list (id, First_Name, Last_Name, Email, Website, Title, Message) VALUES (%r, %r, %r, %r, %r, %r, %r)", (result[i][0], table_list[0], table_list[1], table_list[2], table_list[3], table_list[4], table_list[5]))
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True)
