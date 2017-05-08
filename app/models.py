from app import db


class Post(db.Model):
    __tablename__ = 'post'
    # because it is an existing table
    __table_args__ = {'extend_existing': True}
    id = db.Column('id', db.Integer, primary_key=True)
    body = db.Column('body', db.Text)
    title = db.Column('title', db.VARCHAR)
    developer_id = db.Column('developer_id', db.Integer, db.ForeignKey('developer.developer_id'))
    developer = db.relationship('Developer', backref=db.backref('posts', lazy='dynamic'))
    # first_name = developer.first_name
    # last_name

    created_at = db.Column('created_at', db.VARCHAR)

    def __repr__(self):
        return '{}\t{}'.format(self.title, self.developer_id)


class Developer(db.Model):
    __tablename__ = 'developer'
    # because it is an existing table
    __table_args__ = {'extend_existing': True}
    developer_id = db.Column('developer_id', db.Integer, primary_key=True)
    first_name = db.Column('first_name', db.VARCHAR)
    last_name = db.Column('last_name', db.VARCHAR)
