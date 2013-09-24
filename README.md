# DocJSON tools for Django Rest Framework

Some helper classes and functions for [Django Rest Framework](http://django-rest-framework.org/) for building hypermedia APIs in the [DocJSON document format](https://github.com/docjson/docjson).


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

Subclasses of Django Rest Framework's ``` Serializer ``` and ``` ModelSerializer ``` that wrap serialized data in ``` {'_type': 'list', 'items': '...'} ``` when the serializer is instantiated with ``` many=True ```


### Functions

#### reverse

Same as Django Rest Framework's ``` reverse() ``` but wraps the returned URL in ``` {'_type': 'link': 'href': '...'} ```.


### Generic Views

Define an object with meta or navigation to serialize into your DocJSON document.  Pass that object into your generic view to place the content of your view inside the document.  You can override ``` get_document() ``` or ``` get_document_serializer() ``` on ``` GenericDocJSONAPIView ``` for custom behavior.  Only ``` ListDocJSONAPIView ``` and ``` RetrieveDocJSONAPIView ``` are implemented so far.

** Example: **

    class NavigationDocument(object):
        categories = Category.objects.published().distinct()
        tags = Tag.objects.published().distinct()


    class ArticleList(generics.ListDocJSONAPIView):
        serializer_class = ArticleListSerializer
        queryset = Article.objects.published()
        document_key = 'articles'
        document = NavigationDocument()
        document_serializer = NavigationDocumentSerializer

Visiting the URL that points to ``` ArticleList ``` would return:

	{
	    "categories": {
	    	"_type": "list",
	        "items": [...]
	        }, 
	    "tags": {
	    	"_type": "list",
	        "items": [...]
	    }, 
	    "articles": {
	    	"_type": "list",
	        "items": [...]
	    }
	}
