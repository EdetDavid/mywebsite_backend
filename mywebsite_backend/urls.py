from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Staff Adviser Superadmin"
admin.site.site_title = "Staff Adviser Superadmin Portal"
admin.site.index_title = "Welcome to Staff Sdviser Superadmin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    
]


# Retrieve images from /media/
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
