from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Exercise, WorkOut
from .serializers import ExerciseSerializer, WorkOutSerializer

class ExerciseListView(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ExerciseSerializer(queryset, many=True)
        return Response(serializer.data)

class ExerciseDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
