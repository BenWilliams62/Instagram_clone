from django.contrib import admin
from django.urls import path, include
from .views import (
    home,
    explore,
    activity,
    comments,
    lists,
    single,
    login,
    ProfileView,
    ProfileEditView,
    ImageView,
    login_logic,
    updateLike,
    updateFollow,
    logout_view,
)
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="home"),
    path('home',home, name="home"),
    path('profile/<slug>', ProfileView.as_view(), name='profile'),
    path('profile-edit/<slug>', ProfileEditView.as_view(), name='profile-edit'),
    path('explore', explore, name="explore"),
    path('activity', activity, name="activity"),
    path('comments', comments, name='comments'),
    path('image/<slug>', ImageView.as_view(), name='image'),
    path('lists', lists, name="lists"),
    path('single-image', single, name="single"),


    path('login', login_logic, name="login"),
    path('update_like/', updateLike, name="update_like"),
    path('update_follow/', updateFollow, name="update_follow"),
    path('logout/', logout_view, name="logout"),

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
 