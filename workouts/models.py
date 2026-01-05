from django.db import models

class Workout(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100) # e.g., "Shoulders & Abs"

    def __str__(self):
        return f"{self.date} - {self.name}"

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # e.g., "Shoulder Press"

    def __str__(self):
        return self.name

class ExerciseSet(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='sets', on_delete=models.CASCADE)
    set_number = models.IntegerField()
    weight = models.FloatField()
    reps = models.IntegerField()
    note = models.TextField(blank=True, null=True) # For "form no good" notes

    def __str__(self):
        return f"{self.exercise.name} - Set {self.set_number}"