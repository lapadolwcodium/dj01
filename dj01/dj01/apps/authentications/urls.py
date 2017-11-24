from django.conf.urls import url

from dj01.apps.authentications.views import LoginView, logout_view, SuccessView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout'),

    # TODO This url is meant to be sample you should remove it
    url(r'^success/$', SuccessView.as_view(), name='success'),
]