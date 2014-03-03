from rest_framework import pagination


class DocJSONPaginationSerializer(pagination.BasePaginationSerializer):
    """
    The minimum DocJSON requirement for list pagination
    """
    next = pagination.NextPageField(source='*')
    results_field = 'items'



class DocJSONPaginationSerializerWithPrevious(DocJSONPaginationSerializer):
    """
    DocJSON list pagination with a 'previous' property
    """
    previous = pagination.PreviousPageField(source='*')
