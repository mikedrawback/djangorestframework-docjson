from rest_framework import serializers


class DocJSONSerializerMixin(object):
    pass


class DocJSONSerializer(DocJSONSerializerMixin,
                        serializers.Serializer):
    pass


class DocJSONModelSerializer(DocJSONSerializerMixin,
                             serializers.ModelSerializer):
    pass
