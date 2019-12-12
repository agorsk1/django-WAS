from rest_framework.decorators import action
from rest_framework.response import Response

from contacts.models import Person
from contacts.serializers import PersonSerializer
from rest_framework import generics, viewsets, renderers


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(detail=False, renderer_classes=[renderers.JSONRenderer])
    def pesel(self, request, *args, **kwargs):
        obj = {1, 2, 3, 4, 5}
        return Response(obj)
