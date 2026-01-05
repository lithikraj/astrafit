# workouts/serializers.py
from rest_framework import serializers
from .models import Workout, Exercise, ExerciseSet

class ExerciseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseSet
        fields = ['set_number', 'weight', 'reps', 'note']

class ExerciseSerializer(serializers.ModelSerializer):
    sets = ExerciseSetSerializer(many=True)

    class Meta:
        model = Exercise
        fields = ['name', 'sets']

class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'date', 'name', 'exercises']

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(**validated_data)
        for exercise_data in exercises_data:
            sets_data = exercise_data.pop('sets')
            exercise = Exercise.objects.create(workout=workout, **exercise_data)
            for set_data in sets_data:
                ExerciseSet.objects.create(exercise=exercise, **set_data)
        return workout