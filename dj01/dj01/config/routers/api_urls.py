from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
# Add your API router here. It should be sorted by alphabet.

from dj01.config.logic.test_api import take_json
from dj01.config.logic.test_api_post_param import take_json_post

# For function API view
urlpatterns = [
    url(r'^testapi', take_json, name="export-order_get"),
    url(r'^testapipost/', take_json_post, name="export-order_post")
]

urlpatterns += router.urls
