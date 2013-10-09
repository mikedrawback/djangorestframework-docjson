# DocJSON tools for Django Rest Framework

Some helper classes and functions for [Django REST Framework](http://django-rest-framework.org/) for building hypermedia APIs in the [DocJSON document format](https://github.com/docjson/docjson).


### Fields

#### DocJSONIdentityField

Subclass of ```HyperlinkedIdentityField ``` that wraps the hyperlink in ``` {'_type': 'link': 'href': '...'} ```:

    from rest_framework_docjson.fields import DocJSONIdentityField
    
    class ArticleSerializer(serializers.ModelSerializer):
        permalink = DocJSONIdentityField(view_name='article-detail')

    class Meta:
        model = Article


### Serializers

#### DocJSONSerializer and DocJSONModelSerializer

Subclasses of Django REST Framework's ``` Serializer ``` and ``` ModelSerializer ``` that wrap serialized data in ``` {'_type': 'list', 'items': '...'} ``` when the serializer is instantiated with ``` many=True ```

#### DocJSONPaginationSerializer

Provides the minimum DocJSON requirement for list pagination objects.  Includes a 'next' hyperlink, sets the ``` results_field ``` to ``` 'items' ```.


### Functions

#### reverse

Same as Django Rest Framework's ``` reverse() ``` but wraps the returned URL in ``` {'_type': 'link': 'href': '...'} ```.