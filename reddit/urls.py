"""reddit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from Authentication.views import loginView, logoutView, registerView
from Main.views import IndexView, AllView, subreddit_view
from Post.views import upvote_view, downvote_view, user_view

urlpatterns = [
    path('', IndexView.as_view(), name="homepage"),
    path('r/all/', AllView.as_view()),
    path('r/<str:sub>/', subreddit_view),
    path('u/<str:username>/', user_view),
    path('upvote/post/<int:post_id>', login_required(upvote_view)),
    path('downvote/post/<int:post_id>', login_required(downvote_view)),
    path('accounts/login/', loginView.as_view()),
    path('accounts/logout/', login_required(logoutView.as_view())),
    path('accounts/register/', registerView.as_view()),
    path('admin/', admin.site.urls),
]
