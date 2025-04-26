from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', views.production_list, name='fabric'),
#	path('admin/', admin.site.urls),
    path('', include('employee.urls')),
    path('dpsr/', views.dpsr_log, name='dpsr_log'),
	#path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


