from django.contrib import admin
from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path


urlpatterns = [
    # Admin 
    path('admin/', admin.site.urls),
    # Frontend 
    path('', views.frontend, name="frontend"),
    # Backend 
    path('home/', views.backend, name="backend"),

    # Login/logout
    path('login/', views.Login, name="login"),
    path('login_user/', views.LoginUser, name="login_user"),
    path('logout/', views.LogoutUser, name="logout"),

    # csv
    path('upload_libreria/', views.upload_csv, name="upload_csv"),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)