# DocJSON tools for Django REST Framework

Some helper classes and functions for [Django REST Framework](http://django-rest-framework.org/) for building hypermedia APIs in the [DocJSON document format](https://github.com/docjson/docjson).


### Fields

#### DocJSONIdentityField

Subclass of ```HyperlinkedIdentityField ``` that wraps the hyperlink in ``` {'_type': 'link': 'url': '...'} ```:

    from rest_framework_docjson.fields import DocJSONIdentityField
    
    class ArticleSerializer(serializers.ModelSerializer):
        permalink = DocJSONIdentityField(view_name='article-detail')

    class Meta:
        model = Article


### Functions

#### reverse

Same as Django Rest Framework's ``` reverse() ``` but wraps the returned URL in ``` {'_type': 'link': 'url': '...'} ```.

### Renderers

#### DocJSONRenderer and UnicodeDocJSONRenderer

Adds to top level element ``` {"_type": "document} ``` to the serialized data before rendering.  Also uses the view's ``` get_view_name() ``` and ``` get_view_description() ``` to populate the  ``` "meta": "title" ``` and ``` "meta": "description" ```.

media type:  ``` 'vnd.document+json' ```
format:  ``` 'docjson' ```

In accordance with the [IANA assignment here](http://www.iana.org/assignments/media-types/application/vnd.document+json).
