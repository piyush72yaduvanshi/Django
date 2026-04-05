from django.urls import path
from . import views


urlpatterns = [
    #localhost:8000/chai
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
