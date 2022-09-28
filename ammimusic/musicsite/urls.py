from django.contrib import admin
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('contact/', views.contact),
    path('Register/', views.RegData),
    path('joinus/', views.joinus),
    path('login/', views.login),
    path('logincode/', views.logincode),
    path('admin1/', views.admin),
    path('addcategory/', views.addcategory),
    path('showcategory/', views.showcategory),
    path('addsongs/', views.media),
    path('showsongs/', views.showsongs),
    path('showuser/', views.showuser),
    path('logout/', views.logout),
    path('uaddsongs/', views.umedia),
    path('ushowsongs/', views.ushowsongs),
    path('account/', views.account),
    path('ushowcategory/', views.ushowcategory),
    path('user/', views.user),
    path('changepassword/', views.changepassword),
   
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

