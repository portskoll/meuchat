from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('rooms/', include('room.urls')),
    path('admin/', admin.site.urls),

]
