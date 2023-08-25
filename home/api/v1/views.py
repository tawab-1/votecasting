from rest_framework.viewsets import ModelViewSet
from home.models import Party, Candidate
from home.api.v1.serializers import CandidateSerializer, PartySerializer



class PartyViewSet(ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer