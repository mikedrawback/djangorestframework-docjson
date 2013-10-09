from rest_framework import pagination


class DocJSONPaginationSerializer(pagination.BasePaginationSerializer):
    """
    The minimum DocJSON requirement for list pagination
    """
    next = pagination.NextPageField(source='*')
    results_field = 'items'

    @property
    def data(self):
        """
        wraps the serialized representation in the DocJSON list type
        """
        data = super(DocJSONPaginationSerializer, self).data
        data['_type'] = 'list'
        return data

    def field_to_native(self, obj, field_name):
        """
        wraps the nested representation in the DocJSON list type
        """
        data = super(DocJSONPaginationSerializer, self)\
            .field_to_native(obj, field_name)
        data['_type'] = 'list'
        return data


class DocJSONPaginationSerializerWithPrevious(DocJSONPaginationSerializer):
    """
    DocJSON list pagination with a 'previous' property
    """
    previous = pagination.PreviousPageField(source='*')
