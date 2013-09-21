from rest_framework import serializers


class DocJSONModelSerializer(serializers.ModelSerializer):
    @property
    def data(self):

        data = super(DocJSONModelSerializer, self).data
        if self.many:
            return {'_type': 'list', 'items': [item for item in data]}
        return data

    def field_to_native(self, obj, field_name):
        """
        wraps the nested representation in the DocJSON list type
        """

        data = super(DocJSONModelSerializer, self)\
            .field_to_native(obj, field_name)

        if hasattr(data, '__iter__'):
            return {'_type': 'list', 'items': [item for item in data]}

        return data
