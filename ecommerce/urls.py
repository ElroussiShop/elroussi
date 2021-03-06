from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)