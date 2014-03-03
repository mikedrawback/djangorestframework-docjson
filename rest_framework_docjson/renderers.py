from rest_framework.renderers import JSONRenderer, UnicodeJSONRenderer


class DocJSONRendererMixin(object):
    media_type = 'vnd.document+json'
    format = 'docjson'

    def render(self, data, media_type=None, renderer_context=None):
        """
        adds the top-level docjson elements to the serialized data
        """
        data['_type'] = 'document'
        data['meta'] = {
        	'url': renderer_context['request'].build_absolute_uri(),
        	'title': renderer_context['view'].get_view_name(),
        	'description': renderer_context['view'].get_view_description()
        }

        return super(DocJSONRendererMixin, self).render(data, media_type, renderer_context)


class DocJSONRenderer(DocJSONRendererMixin, JSONRenderer):
	pass


class UnicodeDocJSONRenderer(DocJSONRendererMixin, UnicodeJSONRenderer):
	pass
