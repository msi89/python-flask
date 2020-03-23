from datetime import datetime
from core.exts import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(160))
    body = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def serialize(self):
        return {'id': self.id, 'title': self.title, 'body': self.body,
                'created_at': self.created_at}

