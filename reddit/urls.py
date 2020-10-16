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
from Main.views import IndexView, AllView, subreddit_view, subscribe_action_view
from Post import views as pViews
from User.views import user_view

urlpatterns = [
    path('', IndexView.as_view(), name="homepage"),
    path('r/all/', AllView.as_view()),
    path('post/<int:post_id>/', pViews.post_detail_view),
    path('comment_detail/<int:comment_id/', pViews.comment_detail_view),
    path('r/<str:sub>/', subreddit_view),
    path('r/<str:sub>/subscribe/', subscribe_action_view),
    path('u/<str:username>/', user_view),
    path('upvote/post/<int:post_id>/', login_required(pViews.upvote_post_view)),
    path('downvote/post/<int:post_id>/', login_required(pViews.downvote_post_view)),
    path('upvote/comment/<int:comment_id>/', login_required(pViews.upvote_comment_view)),
    path('downvote/comment/<int:comment_id>/', login_required(pViews.downvote_comment_view)),
    path('accounts/login/', loginView.as_view()),
    path('accounts/logout/', login_required(logoutView.as_view())),
    path('accounts/register/', registerView.as_view()),
    path('admin/', admin.site.urls),
]
