from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from profiles.models import Player
from .serializers import PlayerSerializer


class PlayerAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field            = 'pk' 
    serializer_class        = PlayerSerializer
    permission_classes      = (IsAuthenticated,)
    queryset                = Player.objects.all()
    search_fields           = ('first_name', 'last_name', 'position')

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PlayerRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk'
    serializer_class        = PlayerSerializer
    permission_classes      = (IsAuthenticated,)
    queryset                = Player.objects.all()

    def get_queryset(self):
        return Player.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}