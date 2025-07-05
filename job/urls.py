from django.urls import path
from .views import JobView

urlpatterns = [
    path('jobs/', JobView.as_view(), name='job-list'),
    path('jobs/<int:id>/', JobView.as_view(), name='job-detail'),
]

