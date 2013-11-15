from rest_framework.renderers import JSONRenderer


class DocJSONRenderer(JSONRenderer):
    media_type = 'vnd.document+json'
    format = 'docjson'
