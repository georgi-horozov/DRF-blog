from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.views import PostViewset

router = DefaultRouter()
router.register("", PostViewset, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("posts/", include(router.urls)),
    path("auth/", include("accounts.urls")),
]
