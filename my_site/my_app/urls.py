from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user-detail'),
    path('follow/', FollowViewSet.as_view({'get': 'list', 'post': 'create'}), name='follow-list'),
    path('follow/<int:pk>/', FollowViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='follow-detail'),
    path('post/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('post/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='post-detail'),
    path('post_like/', PostLikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='post_like-list'),
    path('post_like/<int:pk>/', PostLikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='post_like-detail'),
    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment-detail'),
    path('comment_like/', CommentLikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_like-list'),
    path('comment_like/<int:pk>/', CommentLikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='comment_like-detail'),
    path('story/', StoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='story-list'),
    path('story/<int:pk>/',StoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='story-detail'),
    path('group/', GroupViewSet.as_view({'get': 'list', 'post': 'create'}), name='group-list'),
    path('story/<int:pk>/',GroupViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='group-detail'),
]
