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

# Create class for users table
class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column('name', db.Unicode, primary_key= True)
    age = db.Column('age', db.Integer)

another = Users(name='Jake', age=25)
db.session.add(another)
db.session.commit()
all_users = Users.query.filter_by(name='Jake').all()
for siteUser in all_users:
    db.session.delete(siteUser)
db.session.commit()
print(all_users)

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

