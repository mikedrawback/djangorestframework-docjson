from rest_framework import serializers


class DocJSONSerializerMixin(object):
    @property
    def data(self):
        """
        wraps the serialized representation in the DocJSON list type
        """
        data = super(DocJSONSerializerMixin, self).data
        if self.many:
            return {'_type': 'list', 'items': [item for item in data]}

        return data

    def field_to_native(self, obj, field_name):
        """
        wraps the nested representation in the DocJSON list type
        """
        data = super(DocJSONSerializerMixin, self)\
            .field_to_native(obj, field_name)

        if self.many:
            return {'_type': 'list', 'items': [item for item in data]}

        return data


class DocJSONSerializer(DocJSONSerializerMixin,
                        serializers.Serializer):
    pass


class DocJSONModelSerializer(DocJSONSerializerMixin,
                             serializers.ModelSerializer):
    pass
