from core.exts import serializer


class UserSerializer(serializer.Schema):

    class Meta:
        fields = ('id', 'username')
