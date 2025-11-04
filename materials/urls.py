from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register("", CourseViewSet)


urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lessons_list"),
    path("lesson/create", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path("lesson/<int:pk>/update", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path(
        "lesson/<int:pk>/delete", LessonDestroyAPIView.as_view(), name="lessons_delete"
    ),

] + router.urls