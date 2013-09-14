from rest_framework import serializers


class DocJSONModelSerializer(serializers.ModelSerializer):
    @property
    def data(self):
        data = super(DocJSONModelSerializer, self).data
        if self.many:
            return {'_type': 'list', 'items': [item for item in data]}
        return data
