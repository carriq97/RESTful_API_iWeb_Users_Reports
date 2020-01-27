from resources.error_handler import not_found
from dbconfig import mysql
from flask import jsonify, request, Blueprint

from resources.models.user import User

userBP = Blueprint('user', __name__)


def parse_users(user_list):
    resp_data = []
    for u in user_list:
        resp_data.append({"id": u.id, "data": {"id": u.id, "username": u.username, "name": u.name, "email": u.email,
                                               "admin": u.admin_flag}})
    return resp_data


@userBP.route('/local/v1/users', methods=['GET'])
def get_users():
    users = User.query.all()
    resp = jsonify(parse_users(users))
    resp.status_code = 200
    return resp


@userBP.route('/local/v1/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    resp = jsonify(id=user.id, username=user.username, name=user.name, email=user.email, admin_flag=user.admin_flag)
    resp.status_code = 200
    return resp


@userBP.route('/local/v1/users/paramSearch/email/<string:user_email>', methods=['GET'])
def get_user_by_email(user_email):
    user = User.query.get(str(user_email))
    resp = jsonify(id=user.id, username=user.username, name=user.name, email=user.email, admin_flag=user.admin_flag)
    resp.status_code = 200
    return resp


@userBP.route('/local/v1/users/paramSearch/nickname/<string:user_nickname>', methods=['GET'])
def get_user_by_nickname(user_nickname):
    user = User.query.get(str(user_nickname))
    resp = jsonify(id=user.id, username=user.username, name=user.name, email=user.email, admin_flag=user.admin_flag)
    resp.status_code = 200
    return resp


@userBP.route('/local/v1/users/add', methods=['POST'])
def create_user():
    cursor = mysql.connection.cursor()
    try:
        _id = request.args.get('id')
        _nickname = request.args.get('nickname')
        _name = request.args.get('name')
        _email = request.args.get('email')
        _adminFlag = request.args.get('adminFlag')
        if _id and _nickname and _name and _email and _adminFlag:
            sql = 'INSERT INTO usertable(id,nickname,name,email,adminFlag) VALUES(%s,%s,%s,%s,%s)'
            data = (_id, _nickname, _name, _email, _adminFlag)
            cursor.execute(sql, data)
            cursor.connection.commit()
            resp = jsonify('Done!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@userBP.route('/local/v1/users/update', methods=['POST'])
def update_user():
    cursor = mysql.connection.cursor()
    try:
        _id = request.args.get('id')
        _nickname = request.args.get('nickname')
        _name = request.args.get('name')
        _email = request.args.get('email')
        _adminFlag = request.args.get('adminFlag')
        if _id and _nickname and _name and _email and _adminFlag:
            sql = 'UPDATE usertable SET nickname = %s, name = %s, email = %s, adminFlag = %s WHERE id = %s'
            data = (_nickname, _name, _email, _adminFlag, _id)
            cursor.execute(sql, data)
            cursor.connection.commit()
            resp = jsonify('Done!')
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@userBP.route('/local/v1/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute('DELETE FROM userTable WHERE id = %s', [user_id])
        cursor.connection.commit()
        resp = jsonify('Done!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
