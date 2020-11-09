from django.urls import path
from posts.views import posts, post_details

urlpatterns = [
    path('', posts, name="posts"),
    path('postdetail/<int:id>/', post_details, name='post_detail')
]
