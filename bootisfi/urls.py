from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('library', views.library, name="library"),
    path('library/<str:filter>', views.library_filters, name="library_filters"),
    path('profile', views.profile, name="profile"),
    path('login/', views.loginUser, name="login"),
    path('signup/', views.signupUser, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('play/<uuid:song_id>', views.listen, name="play"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)