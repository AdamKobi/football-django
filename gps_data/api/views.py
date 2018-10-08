from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from gps_data.models import RawData
from profiles.models import Player
from .serializers import GpsSerializer


class GpsAPIView(generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = GpsSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes      = (IsAuthenticated,)
    queryset                = RawData.objects.all()
    search_fields           = ('date', 'athlete',)

    # def get_queryset(self):
    #     qs = Injury.objects.all()
    #     query = self.request.GET.get("q")
    #     if query is not None:
    #         qs = qs.filter(
    #                 Q(title__icontains=query)|
    #                 Q(content__icontains=query)
    #                 ).distinct()
    #     return qs

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class GpsRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = GpsSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes      = (IsAuthenticated,)
    queryset                = RawData.objects.all()

    def get_queryset(self):
        return RawData.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}