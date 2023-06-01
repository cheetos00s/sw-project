from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    # Admin 
    path('admin/', admin.site.urls),
    # Frontend 
    path('', views.frontend, name="frontend"),
    # Backend 
    path('backend/', views.backend, name="backend"),

    # Login/logout
    path('login/', views.Login, name="login"),
    path('login_user/', views.LoginUser, name="login_user"),
    path('logout/', views.LogoutUser, name="logout"),

     # PAIS
    # Home page
    path('pais_list/', views.pais_list, name="pais_list"),
    # Path to add product
    path('pais_add',views.pais_add, name='pais_add'),
    # Access product data individually
    path('pais/<str:pais_id>', views.pais, name = "pais_views"),
    # Path to edit product
    path('pais_edit', views.pais_edit, name="pais_edit"),
    # Delete product
    path('pais_delete/<str:pais_id>', views.pais_delete, name="pais_delete"),

]