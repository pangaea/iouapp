from flask import Flask, render_template, json, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import globals
import sys

def signUp(_username, _displayname, _email, _password):
    try:
        # validate the received values
        if _username and _displayname and _email and _password:
            # All fields good !!
            _hashed_password = generate_password_hash(_password)
            #print('Hashed Password => ' + _hashed_password, file=sys.stderr)
            conn = globals.mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_username,_displayname,_email,_hashed_password))
            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'success':'true', 'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'error':'Enter the required fields'})
    finally:
        cursor.close()
        conn.close()

def login(_username, _password):
    try:
        if _username and _password:
            conn = globals.mysql.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT id, password_hash, display_name FROM users WHERE username=%s', (_username,))
            for row in cursor:
                if check_password_hash(row[1], _password):
                    session['username'] = _username
                    session['user_id'] = row[0]
                    session['display_name'] = row[2]
                    return json.dumps({'success':'true', 'message':'User authentication success !'})
                else:
                    return json.dumps({'message':'User authentication failed !'})
            else:
                return json.dumps({'message':'User does not exist !'})
    finally:
        cursor.close()
        conn.close()