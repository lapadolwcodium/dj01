from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
# Add your API router here. It should be sorted by alphabet.

from dj01.config.logic.test_api import take_json

# For function API view
urlpatterns = [
 url(r'^testapi/', take_json, name="export-order")
]

urlpatterns += router.urls