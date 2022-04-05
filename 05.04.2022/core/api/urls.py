from django.urls import path, include
from rest_framework import routers
from api.views import  MainViewSet, ApiNew

router = routers.DefaultRouter()
router.register(r'main', MainViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api2/', ApiNew.as_view())
]