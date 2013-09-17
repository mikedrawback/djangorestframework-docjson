# DocJSON tools for Django Rest Framework

Some helper classes for [Django Rest Framework](http://django-rest-framework.org/) for building hypermedia APIs in the [DocJSON document format](https://github.com/docjson/docjson).

## Usage

There are only two classes so far.

### DocJSONIdentityField

Subclass of ```HyperlinkedIdentityField ``` that wraps the hyperlink in ``` {'_type': 'link': 'href': '...'} ```:

    from rest_framework_docjson.fields import DocJSONIdentityField
    
    class ArticleSerializer(serializers.ModelSerializer):
        permalink = DocJSONIdentityField(view_name='article-detail')

    class Meta:
        model = Article

### DocJSONModelSerializer

Subclass of ``` ModelSerializer ``` that wraps returned data in ``` {'_type': 'list', 'items': '...'} ``` when the serializer is instantiated with ``` many=True ```

