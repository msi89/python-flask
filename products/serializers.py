from core.exts import serializer


class ProductSerializer(serializer.Schema):

    class Meta:
        fields = ('id', 'name', 'description')
