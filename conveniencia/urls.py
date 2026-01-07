from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalogo.admin_viwes import sync_produtos_admin

urlpatterns = [
    path("admin/sync-produtos/", sync_produtos_admin, name="sync_produtos_admin"),
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )