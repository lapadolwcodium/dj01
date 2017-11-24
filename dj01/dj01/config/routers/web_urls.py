from django.conf.urls import url, include

urlpatterns = [
    url(r'^auth/', include('dj01.apps.authentications.urls', namespace='auth')),
]