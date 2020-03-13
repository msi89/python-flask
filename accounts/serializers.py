from core.extensions import serializer


class UserSerializer(serializer.Schema):

    class Meta:
        fields = ('id', 'username')
