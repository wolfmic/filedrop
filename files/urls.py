from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('get/<str:file_id>/', views.get_file, name='get'),
]
