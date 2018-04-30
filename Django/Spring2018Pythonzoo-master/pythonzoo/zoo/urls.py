from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.ZooDetailView.as_view(), name='zooDetail'),

]
