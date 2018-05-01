from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.ZooDetailView.as_view(), name='zooDetail'),
    path('exhibit/<int:pk>', views.ExhibitDetailView.as_view(), name='exhibitDetail'),
    path('animal/<int:pk>', views.AnimalDetailView.as_view(), name='animalDetail'),

]
