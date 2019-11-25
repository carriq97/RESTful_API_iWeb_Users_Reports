from dbconfig import mysql
from flask import jsonify, request, Blueprint
from api.error_handler import not_found


reportBP = Blueprint('report', __name__)


@reportBP.route('/api/v1.0/reports', methods=['GET'])
def get_reports():
    cursor = mysql.connection.cursor()
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


@reportBP.route('/api/v1.0/reports/<int:report_id>', methods=['GET'])
def get_reports_by_id(report_id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute('SELECT * from reporttable WHERE id = %s', [report_id])
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@reportBP.route('/api/v1.0/reports/text/<string:report_text>', methods=['GET'])
def get_reports_by_text(report_text):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute('SELECT * FROM reportTable WHERE text LIKE %s', ['%' + report_text + '%'])
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@reportBP.route('/api/v1.0/reports/add', methods=['POST'])
def create_report():
    cursor = mysql.connection.cursor()
    try:
        _id = request.args.get('id')
        _text = request.args.get('text')
        _image = request.args.get('image')
        _userTable_id = request.args.get('userTable_id')
        if _id and _text and _image and _userTable_id:
            sql = 'INSERT INTO reporttable(text,image,userTable_id) VALUES(%s,%s,%s)'
            data = (_text, _image, _userTable_id)
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


@reportBP.route('/api/v1.0/reports/update', methods=['POST'])
def update_report():
    cursor = mysql.connection.cursor()
    try:
        _id = request.args.get('id')
        _text = request.args.get('text')
        _image = request.args.get('image')
        _userTable_id = request.args.get('userTable_id')
        if _id and _text and _image and _userTable_id:
            sql = 'UPDATE reporttable SET text = %s, image = %s, userTable_id = %s WHERE id = %s'
            data = (_text, _image, _userTable_id, _id)
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


@reportBP.route('/api/v1.0/reports/delete/<int:report_id>', methods=['POST'])
def delete_report(report_id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute('DELETE FROM reporttable WHERE id = %s', [report_id])
        cursor.connection.commit()
        resp = jsonify('Done!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()


@reportBP.route('/api/v1.0/reports/user/<string:user_id>', methods=['GET'])
def get_reports_by_user(user_id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute('SELECT B.* FROM reportTable B WHERE B.userTable_id = (SELECT A.id FROM usertable A WHERE A.id = %s)', [user_id])
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()


