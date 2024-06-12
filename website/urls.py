from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),  # Uncomment this line if you have a login view
    path('logout/', views.logout_user, name='logout'),
]
