from core.exts import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=None), unique=True, nullable=False)
    created_on = db.Column(db.DateTime(), server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=None), unique=True, nullable=False)
    slug = db.Column(db.String(length=None), unique=True, nullable=False)
    price = db.Column(db.Integer, default=0, nullable=True)
    details = db.Column(db.String(length=None), nullable=True)
    description = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(
        db.DateTime, server_default=db.func.now(),
        server_onupdate=db.func.now())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))
