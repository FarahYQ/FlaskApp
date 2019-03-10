from flask import Flask, render_template, request
from flask_mysql import MySQL
import yaml


app = Flask(__name__)

# Configure MySQL database
db = yaml.load(open('dbconfig.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_details = request.form
        name = user_details['name']
        age = user_details['age']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        mysql.connection.commit()
        cur.close()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)

