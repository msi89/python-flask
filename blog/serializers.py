from core.exts import serializer


class PostSerialiser(serializer.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'created_at')
