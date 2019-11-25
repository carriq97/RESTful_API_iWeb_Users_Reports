from app.dbconfig import mysql
from flask import jsonify, request, Blueprint
from app.app import not_found


reportBP = Blueprint('report', __name__)


@reportBP.route('/api/v1.0/reports', methods=['GET'])
def get_reports():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * from reporttable')
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@reportBP.route('/api/v1.0/reports/<int:report_id>', methods=['GET'])
def get_reports_by_id(report_id):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * from reporttable WHERE id = %s", report_id)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@reportBP.route('/api/v1.0/reports/text/<string:report_text>', methods=['GET'])
def get_reports_by_text(report_text):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM reportTable WHERE text LIKE %s", ('%' + report_text + '%'))
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@reportBP.route('/api/v1.0/reports/add', methods=['POST'])
def create_report():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        _id = request.args.get('id')
        _text = request.args.get('text')
        _image = request.args.get('image')
        _userTable_id = request.args.get('userTable_id')
        if  _id and _text and _image and _userTable_id:
            sql = "INSERT INTO reporttable(text,image,userTable_id) VALUES(%s,%s,%s)"
            data = (_text, _image, _userTable_id)
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


@reportBP.route('/api/v1.0/reports/update', methods=['POST'])
def update_report():
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        _id = request.args.get('id')
        _text = request.args.get('text')
        _image = request.args.get('image')
        _userTable_id = request.args.get('userTable_id')
        if _id and _text and _image and _userTable_id:
            sql = "UPDATE reporttable SET text = %s, image = %s, userTable_id = %s WHERE id = %s"
            data = (_text, _image, _userTable_id, _id)
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


@reportBP.route('/api/v1.0/reports/delete/<int:report_id>', methods=['GET'])
def delete_report(report_id):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM reporttable WHERE id = %s", report_id)
        connection.commit()
        resp = jsonify('Done!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


@reportBP.route('/api/v1.0/reports/user/<string:user_id>', methods=['GET'])
def get_reports_by_user(user_id):
    connection = mysql.connect()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT B.* FROM reportTable B WHERE B.userTable_id = (SELECT A.id FROM usertable A WHERE A.id = %s)",user_id)
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


