from django.urls import path
import News.views as views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns = [
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = "post_delete"),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = "post_edit"),
    path('post/new/', BlogCreateView.as_view(), name = "post_new"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = "post_detail"),

    path('', BlogListView.as_view(), name='home'),
]
