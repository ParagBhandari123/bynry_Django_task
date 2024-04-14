from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.home, name='home'),
    
    path('hello/', views.hell, name='hell'),
    path('display/', views.display, name='display'),
    path('detailsform/', views.detailsform, name='detailsform'),
    path('fail/', views.fail, name='fail'),
    path('check_info/', views.check_info, name='check_info'), 
    path('check/', views.check, name='check'),
    path('maker/', views.maker, name='maker'),
    path('make/', views.make, name='make'),
    path('track_request/', views.track_request, name='track_request'),
    path('manage_request/', views.manage_request, name='manage_request'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



