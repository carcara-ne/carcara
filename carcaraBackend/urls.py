from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('relationship/scatter', views.relationship, name='relationship'),
    path('composition/pie', views.composition, name='composition'),
    path('distribution/scatter', views.distribution, name='distribution'),
    path('comparison/column', views.comparison, name='comparison'),
]
