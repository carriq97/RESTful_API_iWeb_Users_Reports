from app import app
from error_handler import not_found
from dbconfig import mysql
from flask import jsonify, request


@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * from usertable')
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * from usertable WHERE id = %s", user_id)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/paramSearch/email/<string:user_email>', methods=['GET'])
def get_user_by_email(user_email):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM userTable WHERE email = %s", user_email)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/paramSearch/text/<string:user_text>', methods=['GET'])
def get_user_by_text(user_text):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM userTable WHERE nickname LIKE %s", ('%' + user_text + '%'))
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/paramSearch/nickname/<string:user_nickname>', methods=['GET'])
def get_user_by_nickname(user_nickname):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM userTable WHERE nickname = %s", user_nickname)
        rows = cursor.fetchone()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/add', methods=['POST'])
def create_user():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        _id = request.args.get('id')
        _nickname = request.args.get('nickname')
        _name = request.args.get('name')
        _email = request.args.get('email')
        _adminFlag = request.args.get('adminFlag')
        if _id and _nickname and _name and _email and _adminFlag:
            sql = "INSERT INTO usertable(id,nickname,name,email,adminFlag) VALUES(%s,%s,%s,%s,%s)"
            data = (_id, _nickname, _name, _email, _adminFlag)
            cursor.execute(sql, data)
            connection.commit()
            resp = jsonify('Done!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/update', methods=['POST'])
def update_user():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        _id = request.args.get('id')
        _nickname = request.args.get('nickname')
        _name = request.args.get('name')
        _email = request.args.get('email')
        _adminFlag = request.args.get('adminFlag')
        if _id and _nickname and _name and _email and _adminFlag:
            sql = "UPDATE usertable SET nickname = %s, name = %s, email = %s, adminFlag = %s WHERE id = %s"
            data = (_nickname, _name, _email, _adminFlag, _id)
            cursor.execute(sql, data)
            connection.commit()
            resp = jsonify('Done!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@app.route('/api/v1.0/users/delete/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM userTable WHERE id = %s", user_id)
        connection.commit()
        resp = jsonify('Done!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)