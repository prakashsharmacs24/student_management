from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register('student', views.StudentView, base_name='student')
router.register('school', views.SchoolView, base_name='school')

urlpatterns = router.urls