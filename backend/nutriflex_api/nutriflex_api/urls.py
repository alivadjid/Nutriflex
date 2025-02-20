"""
URL configuration for nutriflex_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .docs_schema import schema_view
from fitness_plan import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/users/', include('account.urls')),
    path('api/workout-plan/<int:user_id>', views.UserWorkoutPlanView.as_view(), name='list-workout'),
    path('api/workout-plan/create', views.WorkoutPlanCreateAPIView.as_view(), name='create-workoutplan'),
    path('api/workout-plans/view/', views.WorkOutPlanListView.as_view(), name="workout-plan-list"),
    path('api/workout-plan/tasks/<str:workoutplan_id>', views.TaskListView.as_view(), name='task-list'),
    path('api/workout-plan/tasks/completed/<str:workoutplan_id>', views.TaskListViewCompleted.as_view(), name="task-list-completed"),
    path('api/workout-plan/task/set_complete_status/<int:task_id>', views.SetTaskCompleted.as_view(), name='set-task-complete-status'),
    path('api/workout-plan/task/set_task_skipped/<int:task_id>', views.SetTaskSkipped.as_view(), name="set-task-skipped-status"),
    path('api/workout-plan/nutrition', views.NutritionMealViewSet.as_view({'get': 'list'}),name='nutrition-list-iems'),
    path('api/workout-plan/task/update_task/<str:workout_plan_id>', views.UpdateTasksView.as_view(), name='update-tasks')
]
