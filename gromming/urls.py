from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),                # 👈 added views.
    path('register/', views.register, name='register'), 
    path('login/', views.login_user, name='login'),    
    path('logout/', views.logout_user, name='logout'), 
    path('services/', views.service, name='services'),
    path('get_user/', views.get_user, name='get_user'),
    path('customize/', views.customize_package_view, name='customize_package'),
    path('mybookings/', views.my_bookings, name='my_bookings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
