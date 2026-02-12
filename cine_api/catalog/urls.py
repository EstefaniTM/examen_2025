from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, CineViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet, basename="marcas")
router.register(r"Cines", CineViewSet, basename="Cines")

urlpatterns = []
urlpatterns += router.urls