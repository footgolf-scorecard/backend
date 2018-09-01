from django.conf.urls import url, include
from rest_framework import routers
from v1 import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'holes', views.HoleViewSet)
router.register(r'scores', views.ScoreViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
