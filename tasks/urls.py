from django.urls import include, path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "tasks"

urlpatterns = [
    path("create/",login_required(views.CreateTask.as_view()),name="create_task"),
    # path("delete/<int:pk>/",login_required(views.DeleteTask.as_view()),name="delete_task"),
    # path("update/<int:pk>/",login_required(views.UpdateTask.as_view()),name="update_task"),
    path('accounts/', include('django.contrib.auth.urls')),
]