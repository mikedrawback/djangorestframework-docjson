from rest_framework.generics import GenericAPIView
import mixins


class GenericDocJSONAPIView(GenericAPIView):
    document = None
    document_serializer = None
    document_key = 'content'

    def get_document(self):
        return self.document

    def get_document_serializer(self, *args, **kwargs):
        return self.document_serializer(*args, **kwargs)


class ListDocJSONAPIView(mixins.ListDocJSONModelMixin,
                         GenericDocJSONAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveDocJSONAPIView(mixins.RetrieveDocJSONModelMixin,
                             GenericDocJSONAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
