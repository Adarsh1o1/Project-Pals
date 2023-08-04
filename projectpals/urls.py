"""projectpals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginpage, name='loginpage'),
    path('home1/', views.home, name='home1'),
    path('logout/', views.Logout, name='logout'),
    path('categories/', views.categories, name='category'),
    path('', views.posts, name='home'),
    path('mail/<int:pk>/<int:pk1>/', views.sendmail, name='mail'),
    path('home/upload',views.uploadpost,name='upload'),
    path('embedded/',views.embedded,name='embedded'),
    path('electronics/',views.electronics,name='electronics'),
    # path('post/<int:pk>/', post_detail, name='post_detail')
    # path('msg/',views.msg,name='msg'),
    # path('username/',views.username,name='username')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

