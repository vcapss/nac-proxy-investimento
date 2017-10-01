from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from proxy.core.models import Pacote
from proxy.core.serializers import PacoteSerializer


class PacoteList(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer


class PacoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer
