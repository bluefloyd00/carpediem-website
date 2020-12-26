from django.urls import path

from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)