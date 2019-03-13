from flask import Flask, render_template, request, jsonify
import dbconfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure MySQL database
db_info = dbconfig.db_info
user = db_info['mysql_user']
pw = db_info['mysql_password']
host = db_info['mysql_host']
db_name = db_info['mysql_db']
db_uri = f'mysql://{user}:{pw}@{host}/{db_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)


@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch the form data
        print(request.form)
        return jsonify({'name': request.form['name'], 'age': int(request.form['age'])})
    return render_template('index.html')

@app.route("/users/<int:num>")
def showUser(num):
    return jsonify({'userId': num})

if __name__ == "__main__":
    app.run(debug = True)

