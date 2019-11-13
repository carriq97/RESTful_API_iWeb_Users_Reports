import pymysql
from app import app
from dbconfig import mysql
from flask import jsonify, flash, request

@app.route('/api/v1.0/users', methods=['GET'])
def get_users():
        try:
                connection = mysql.connect()
                cur = connection.cursor(pymysql.cursors.DictCursor)
                cur.execute('SELECT * from usertable;')
                rows = cur.fetchall()
                resp = jsonify(rows)
                resp.status_code = 200
                return resp
        except Exception as e:
                print(e)
        finally:
                cur.close()
                connection.close()

@app.route('/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
        try:
                connection = mysql.connect()
                cur = connection.cursor(pymysql.cursors.DictCursor)
                query = """ SELECT * from usertable WHERE id = %s """
                cur.execute(query,user_id)
                rows = cur.fetchall()
                resp = jsonify(rows)
                resp.status_code = 200
                return resp
        except Exception as e:
                print(e)
        finally:
                cur.close()
                connection.close()

#To do
@app.route('/api/v1.0/users/<string:nickname>/<string:name>/<string:email>/<int:adminFlag>', methods=['GET'])
def create_user(nickname,name,email,adminFlag):
    connection = mysql.connect()
    cur = connection.cursor(pymysql.cursors.DictCursor)
    cur.execute('SELECT * from usertable;')
    rows = cur.fetchall()
    query = """ INSERT INTO usertable VALUES(%s,%s,%s,%s,%s) """
    args = (len(rows),nickname,name,email,adminFlag)
    cur.execute(query,args)
    cur.execute('SELECT * from usertable;')
    rows = cur.fetchall()
    resp =jsonify(rows)
    resp.status_code = 201
    return  resp


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
