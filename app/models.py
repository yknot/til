from app import db


class Posts(db.Model):
    __tablename__ = 'posts'
    # because it is an existing table
    __table_args__ = {'extend_existing': True}
    id = db.Column('id', db.Integer, primary_key=True)
    body = db.Column('body', db.Text)
    title = db.Column('title', db.VARCHAR)

    def __repr__(self):
        return '<Body %r>' % (self.body)
