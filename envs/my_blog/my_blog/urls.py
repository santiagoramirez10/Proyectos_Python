from django.contrib import admin
from django.urls import path
from posts.views import HelloWorld
from posts.api.views import PostApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',HelloWorld.as_view()),
    path('api/posts',PostApiView.as_view())

]
