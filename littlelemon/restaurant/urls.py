from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r'menu', views.MenuViewSet)
router.register(r'booking', views.BookingViewSet)

urlpatterns = router.urls

