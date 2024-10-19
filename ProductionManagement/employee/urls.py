from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add your home view if not already present
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
 	path('about-us/', views.about_us, name='about'),
    path('production-report/', views.production_report, name='production_report'),
    path('log-report/', views.log_report, name='log_report'),
]