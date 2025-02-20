# account/models.py
import uuid
import json
from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class NutritionMeal(models.Model):
    description = models.CharField(max_length=255)
    food_suggestions = models.JSONField()
    calories = models.IntegerField()
    recently_issued = models.BooleanField(default=True)
    

    def __str__(self):
        self.food_suggestion_string = json.dumps(self.food_suggestions)
        return f" {self.id} | {self.food_suggestion_string}"


class Task(models.Model):
    description = models.TextField()
    is_done = models.BooleanField(default=False, null=False)
    skipped = models.BooleanField(default=False, null=False)
    duration = models.CharField(max_length=20, null=True)
    day_to_be_done = models.DateField(auto_now_add=False, null=True)
    

    def __str__(self):
        return f"{self.id} | {self.description}"


class WorkoutPlan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default="Sample WorkoutPlan", max_length=20)
    fitness_profile_name = models.CharField(max_length=255, null=True)
    description = models.TextField()  
    tasks = models.ManyToManyField(Task, blank=True)
    nutrition_meals = models.ManyToManyField(NutritionMeal, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fitness_profile_name} | Workout"


class FitnessProfile(models.Model):
    user = models.OneToOneField("account.Account", on_delete=models.CASCADE)
    height = models.FloatField(null=False,blank=False)
    weight = models.FloatField(null=False,blank=False)
    bmi = models.FloatField(null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    goals = models.TextField(null=False, blank=False)
    activity_level = models.CharField(max_length=255, null=False,blank=False)
    smoking_habit = models.CharField(null=False, max_length=255,blank=False)   

    dietary_preference = models.CharField(null=False, max_length=255, blank=False, default="No Idea")
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.SET_NULL, null=True, blank=True)
   
    def calculate_bmi(self):
        # BMI calculation: BMI = weight (kg) / (height (m))^2
        height_in_meters = self.height / 100  # Convert height to meters
        return round(self.weight / (height_in_meters ** 2), 2)

    def get_workout_plan(self):
        pass
        
    def save(self, *args, **kwargs):

        # Automatically calculate and save BMI when saving the object
        self.bmi = self.calculate_bmi()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} - Fitness Plan"
