# from django.urls import path
# from . import views

# app_name = "myapp"

# urlpatterns = [
#     path("",views.IndexView.as_view(), name="index"),
#     path("<int:pk>/",views.DetailView.as_view(),name="detail"),
#     path("<int:pk>/results",views.ResultsView.as_view(),name="results"),
#     path("<int:question_id>/vote",views.vote,name="vote"),
# ]
from django.urls import include, path
from django.contrib.auth.decorators import login_required

from . import views
app_name = "myapp"
urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="index"),
    path("<int:pk>/", login_required(views.DetailView.as_view()), name="detail"),
    path("<int:pk>/results/", login_required(views.ResultView.as_view()), name="results"),
    path("<int:question_id>/vote/", login_required(views.vote), name="vote"),
    path('accounts/', include('django.contrib.auth.urls')),  # Incluir aquí también si es necesario
]