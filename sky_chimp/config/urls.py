from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('', include('app_main.urls', namespace='app_main')),
    path('admin/', admin.site.urls),
    path('blog/', include('app_blog.urls', namespace='app_blog')),
    path('user/', include('app_user.urls', namespace='app_user')),
    path('client/', include('app_client.urls', namespace='app_client')),
    path('message/', include('app_message.urls', namespace='app_message')),
    path('newsletter/', include('app_newsletter.urls', namespace='app_newsletter'))
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
