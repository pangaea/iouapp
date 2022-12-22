from flask import Flask, render_template, request, session, redirect, json
from flaskext.mysql import MySQL

import controllers.authentication
import controllers.iou_controller
import globals

app = Flask(__name__)
app.secret_key = "1234567890"

with open('config.json') as config_file:
    config_data = json.load(config_file)
    
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = config_data['database']['MYSQL_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = config_data['database']['MYSQL_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = config_data['database']['MYSQL_DB']
app.config['MYSQL_DATABASE_HOST'] = config_data['database']['MYSQL_HOST']

globals.mysql = MySQL()
globals.mysql.init_app(app)

@app.route("/")
def main():
    if session.get('username') == None:
        return redirect("/login", code=302)
    return controllers.iou_controller.query()

@app.route('/signup')
def signup():
    return render_template('signup.html', signup_active="active", in_session="false")

@app.route('/login')
def login():
    return render_template('login.html', login_active="active", in_session="false")

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect("/login", code=302)

@app.route('/create_iou')
def create_iou():
    return controllers.iou_controller.render_create()

@app.route('/delete_iou')
def delete_iou():
    iou_id = username = request.args.get('id')
    return controllers.iou_controller.delete(iou_id)

@app.route('/api/signup',methods=['POST'])
def apiSignup():
    _username = request.form['inputUserName']
    _displayname = request.form['inputDisplayName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    return controllers.authentication.signUp(_username, _displayname, _email, _password)

@app.route('/api/login',methods=['POST'])
def apiLogin():
    _username = request.form['inputUserName']
    _password = request.form['inputPassword']
    return controllers.authentication.login(_username, _password)

@app.route('/api/create_iou',methods=['POST'])
def apiCreateIou():
    _user_id = request.form['toUserId']
    _how_much = request.form['inputHowMuch']
    return controllers.iou_controller.create(_user_id, _how_much)

if __name__ == "__main__":
    app.run()