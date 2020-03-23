from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from flask_marshmallow import Marshmallow
from .helpers import CustomBaseQuery

db = SQLAlchemy(query_class=CustomBaseQuery)
guard = Praetorian()
serializer = Marshmallow()
