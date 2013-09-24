from rest_framework import mixins
from rest_framework.response import Response


class ListDocJSONModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        response = super(ListDocJSONModelMixin, self)\
            .list(request, *args, **kwargs)

        document = self.get_document_serializer(
            self.get_document(),
            context={'request': request}).data

        document[self.document_key] = response.data

        response.data = document
        return response


class RetrieveDocJSONModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        response = super(RetrieveDocJSONModelMixin, self)\
            .retrieve(request, *args, **kwargs)

        document = self.get_document_serializer(
            self.get_document(),
            context={'request': request}).data

        document[self.document_key] = response.data

        response.data = document
        return response
