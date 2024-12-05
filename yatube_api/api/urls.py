from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views


from .views import PostViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>[\w.]+)/comments', CommentViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
