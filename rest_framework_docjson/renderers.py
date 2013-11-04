from rest_framework.renderers import JSONRenderer


class DocJSONRenderer(JSONRenderer):
    media_type = 'application/vnd.document+json'
    format = 'docjson'
