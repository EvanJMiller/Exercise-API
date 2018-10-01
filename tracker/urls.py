
from .views import ExerciseDetailView, ExerciseListView
from rest_framework.urls import url

urlpatterns = [
    url(r'^exercises/$', ExerciseListView.as_view()),
    url(r'^exercises/(?P<pk>[0-9]+)$', ExerciseDetailView.as_view())
]