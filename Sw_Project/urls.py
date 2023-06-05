from django.contrib import admin
from django.urls import path
from App import views
from django.conf.urls.static import static
from django.conf import settings

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

    # PAIS
    path('pais_list/', views.pais_list, name="pais_list"),
    # Path to add 
    path('pais_add',views.pais_add, name='pais_add'),
    # Access data individually
    path('pais/<str:pais_id>', views.pais, name = "pais_views"),
    # Path to edit 
    path('pais_edit', views.pais_edit, name="pais_edit"),
    # Delete 
    path('pais_delete/<str:pais_id>', views.pais_delete, name="pais_delete"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)