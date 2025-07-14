from sampleapi.views import StudentView
from django.urls import path

urlpatterns=[
    path('good/',StudentView.as_view()),
]