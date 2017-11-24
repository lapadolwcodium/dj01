from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('dj01.config.routers.api_urls', namespace='api')),
    url(r'^', TemplateView.as_view(template_name="index.html"), name='home'),#include('dj01.config.routers.web_urls'))
    # url(r'/', TemplateView.as_view(template_name="index.html"), name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]
