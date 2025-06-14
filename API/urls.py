from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, register, login
#from .views import register, login
from rest_framework.routers import DefaultRouter
#from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', register),
    path('login/', login),
]


