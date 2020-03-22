from core.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id
