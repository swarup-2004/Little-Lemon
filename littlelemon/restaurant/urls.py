from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter(trailing_slash=False)

router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)


urlpatterns = [
    path('api-token-auth', obtain_auth_token),
    path('', include(router.urls)),

]

