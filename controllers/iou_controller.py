from flask import Flask, render_template, session, json, redirect
import globals

def query():
    try:
        conn = globals.mysql.connect()
        cursor = conn.cursor()
        user_id = session["user_id"]
        cursor.execute('SELECT owed, from_user_id, users.display_name, iou.id FROM iou INNER JOIN users ON users.id = from_user_id WHERE to_user_id=%s', user_id)
        owed_to = cursor.fetchall()

        cursor.execute('SELECT owed, to_user_id, users.display_name, iou.id FROM iou INNER JOIN users ON users.id = to_user_id WHERE from_user_id=%s', user_id)
        owed_from = cursor.fetchall()

        return render_template('index.html', home_active="active", owed_from=owed_from, owed_to=owed_to)
    finally:
        cursor.close()
        conn.close()

def render_create():
    try:
        conn = globals.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id, display_name FROM users')
        users = cursor.fetchall()
        return render_template('create_iou.html', iou_active="active", in_session="true", username=session["username"],
            users=users)
    finally:
        cursor.close()
        conn.close()

def create(to_user_id, how_huch):
    try:
        conn = globals.mysql.connect()
        cursor = conn.cursor()
        user_id = session["user_id"]
        cursor.execute('INSERT INTO iou (owed, to_user_id, from_user_id) VALUES (%s, %s, %s)',
            (how_huch, to_user_id, user_id))
        conn.commit()
        return json.dumps({'success':'true', 'message':'User authentication success !'})
    except:
        return json.dumps({'error':"There was an error"})
    finally:
        cursor.close()
        conn.close()

def delete(id):
    try:
        conn = globals.mysql.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM iou where id=%s', id)
        conn.commit()
        return redirect("/", code=302)
    finally:
        cursor.close()
        conn.close()