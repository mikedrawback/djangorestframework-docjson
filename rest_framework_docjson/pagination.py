from rest_framework import pagination


class DocJSONPaginationFieldMixin(object):

	def to_native(self, value):
		url = super(DocJSONPaginationFieldMixin, self).to_native(value)
		if url:
			return {
				'_type': 'link',
				'url': url
			}
		return


class DocJSONNextPageField(DocJSONPaginationFieldMixin, pagination.NextPageField):
	pass

class DocJSONPreviousPageField(DocJSONPaginationFieldMixin, pagination.PreviousPageField):
	pass


class DocJSONPaginationSerializer(pagination.BasePaginationSerializer):
    """
    wraps the 'Next' page url in the DocJSON link format
    """
    next = DocJSONNextPageField(source='*')
    results_field = 'items'



class DocJSONPaginationSerializerWithPrevious(DocJSONPaginationSerializer):
    """
    wraps the 'Next' and 'Previous' page url in the DocJSON link format
    """
    previous = DocJSONPreviousPageField(source='*')
