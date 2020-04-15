from core.exts import serializer
from marshmallow import fields


class CategorySerializer(serializer.Schema):

    class Meta:
        fields = ['id', 'name', 'created_on', 'updated_on']


class ProductSerializer(serializer.Schema):

    id = fields.Int()
    name = fields.Str()
    category = fields.Nested('CategorySerializer', many=False)
