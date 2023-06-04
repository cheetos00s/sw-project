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
    path('backend/', views.backend, name="backend"),

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

    # FACULTAD
    path('facultad_list/', views.facultad_list, name="facultad_list"),
    # Path to add 
    path('facultad_add',views.facultad_add, name='facultad_add'),
     # Access data individually
    path('facultad/<str:facultad_id>', views.facultad, name = "facultad_views"),
    # Path to edit 
    path('facultad_edit', views.facultad_edit, name="facultad_edit"),
    # Delete 
    path('facultad_delete/<str:facultad_id>', views.facultad_delete, name="facultad_delete"),

    # INSTITUCION
    path('institucion_list/', views.institucion_list, name="institucion_list"),
    # Path to add 
    path('institucion_add',views.institucion_add, name='institucion_add'),
    # Access data individually
    path('institucion/<str:institucion_id>', views.institucion, name = "institucion_views"),
    # Path to edit 
    path('institucion_edit', views.institucion_edit, name="institucion_edit"),
    # Delete 
    path('institucion_delete/<str:institucion_id>', views.institucion_delete, name="institucion_delete"),

    # EMPRESA
    path('empresa_list/', views.empresa_list, name="empresa_list"),
    # Path to add 
    path('empresa_add',views.empresa_add, name='empresa_add'),
    # Access data individually
    path('empresa/<str:empresa_id>', views.empresa, name = "empresa_views"),
    # Path to edit 
    path('empresa_edit', views.empresa_edit, name="empresa_edit"),
    # Delete 
    path('empresa_delete/<str:empresa_id>', views.empresa_delete, name="empresa_delete"),

    # CIUDAD
    path('ciudad_list/', views.ciudad_list, name="ciudad_list"),
    # Path to add 
    path('ciudad_add',views.ciudad_add, name='ciudad_add'),
    # Access data individually
    path('ciudad/<str:ciudad_id>', views.ciudad, name = "ciudad_view"),
    # Path to edit 
    path('ciudad_edit', views.ciudad_edit, name="ciudad_edit"),
    # Delete 
    path('ciudad_delete/<str:ciudad_id>', views.ciudad_delete, name="ciudad_delete"),

    


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)