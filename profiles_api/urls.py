from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
#Here we are not using a base_name since we are using a queryset & django automatically figures out a base name. If we want to over write the default base name, then we specify one.
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
