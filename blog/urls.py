from django.urls import path
from . import views
from users import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
# ,PostDeleteView1


urlpatterns = [
    path('', user_views.comm, name='users-home'),
    path('about/', views.about, name='blog-about'),
    path('home/', views.user_auth, name='users-auth'),
    path('admin1/', views.user_admin, name='users-admin'),
    path('post/<str:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postcreate/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('book/delete/', PostDeleteView1.as_view(), name='post-delete1'),
]
