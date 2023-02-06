from django.urls import path, re_path
from . import views

app_name = 'features'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('guide', views.guide, name='guide'),
    path('submit', views.submit, name='submit'),
    path('send_mail_with_file', views.send_mail_with_file, name='send_mail_with_file'),
    path('database', views.database, name='database'),
    path('download', views.download, name='download'),
]