from rest_framework import relations


class DocJSONIdentityField(relations.HyperlinkedIdentityField):
    def get_url(self, *args, **kwargs):
        url = super(DocJSONIdentityField, self).get_url(*args, **kwargs)
        return {
            '_type': 'link',
            'href': url
        }
