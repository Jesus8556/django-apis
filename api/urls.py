from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cuenta',views.CuentaView,basename="cuenta")
router.register(r'key', views.KeyView, basename="key")
router.register(r'alumno', views.AlumnoView, basename="alumno")
router.register(r'inscripcion', views.InscripcionView, basename="inscripcion")
router.register(r'curso', views.CursoView, basename="curso")
urlpatterns = [
    path('admin/',include(router.urls))
]