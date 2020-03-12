from myapp.settings import serializer


class UserSerializer(serializer.Schema):

    class Meta:
        fields = ('id', 'username')
