from .db import db


class Report(db.Model):
    __tablename__ = 'reportTable'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(100), nullable=True)
    user_table_id = db.Column(db.Integer, db.ForeignKey('userTable.id'), name='userTable_id', nullable=False)
    user = db.relationship('User', backref=db.backref('reportTable', lazy=True))
