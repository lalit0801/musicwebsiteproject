from django.contrib import admin
from django.urls import path,include 
from musicsite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicsite.urls')),
    path('home/', include('musicsite.urls')),
    path('contact/', include('musicsite.urls')),
    path('Register/', include('musicsite.urls')),
    path('joinus/', include('musicsite.urls')),
    path('login/', include('musicsite.urls')),
    path('logincode/', include('musicsite.urls')),
    path('admin1/', include('musicsite.urls')),
    path('showcategory/', include('musicsite.urls')),
    path('addcategory/', include('musicsite.urls')),
    path('addsongs/', include('musicsite.urls')),
    path('showsongs/', include('musicsite.urls')),
    path('showuser/', include('musicsite.urls')),
    path('logout/', include('musicsite.urls')),
    path('uaddsongs/', include('musicsite.urls')),
    path('ushowsongs/', include('musicsite.urls')),
    path('account/', include('musicsite.urls')),
    path('ushowcategory/', include('musicsite.urls')),
    path('user/',include('musicsite.urls') ),
    path('changepassword/',include('musicsite.urls') ),

]
