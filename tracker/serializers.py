from rest_framework import serializers

from .models import Exercise, WorkOut

class ExerciseSerializer(serializers.ModelSerializer):

    workout = serializers.StringRelatedField(many=True)

    class Meta:
        model = Exercise
        fields = ('name', 'date','workout', 'type', 'weight', 'sets', 'duration', 'muscle_target')

class WorkOutSerializer(serializers.Serializer):

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = WorkOut
        fields = ('name', 'date', 'owners', 'exercises')
