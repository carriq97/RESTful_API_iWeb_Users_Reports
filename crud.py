import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify, flash, request


@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
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
def get_user(user_id):
    try:
        connection = mysql.connect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
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


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == '__main__':
    app.run(debug=True)
