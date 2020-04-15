from core.exts import serializer


class PostSerialiser(serializer.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'created_at')


def serialize(data, many=False):
    return PostSerialiser(many=many).dump(data)


def validate(data):
    return PostSerialiser().validate(data)
