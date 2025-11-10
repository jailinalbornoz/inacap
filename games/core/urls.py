from django.urls import path
from django.urls.conf import include
from . import views

from .views import ProductoViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('productos',ProductoViewSet)

urlpatterns = [
    
    path('', views.home, name='home'),

    
    path("productos/", views.producto_list, name="producto_list"),
    path("productos/nuevo/", views.producto_create, name="producto_create"),
    path("productos/<int:pk>/", views.producto_detail, name="producto_detail"),
    path("productos/<int:pk>/editar/", views.producto_edit, name="producto_edit"),
    path("productos/<int:pk>/eliminar/", views.producto_delete, name="producto_delete"),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
