from django.conf.urls import url
from rest_framework import routers


from dj01.config.logic.test_api import take_json
from dj01.config.logic.test_api_post_param import take_json_post


from dj01.config.logic.test_view_01 import ListUsers

snippet_list = ListUsers.as_view({
    'get': 'list',
})

user_detail = ListUsers.as_view({
    'get': 'retrieve'
})

router = routers.DefaultRouter()
# router.register(r'asnippet_list', snippet_list , base_name='snippet_list1')
# router.register(r'auser_detail', user_detail , base_name='user_detail1')
router.register(r'snippets/', ListUsers , base_name='announcement')
# Add your API router here. It should be sorted by alphabet.



# For function API view
urlpatterns = [
    url(r'^testapi/', take_json, name="export-order_get"),
    url(r'^testapipost/', take_json_post, name="export-order_post")
]

urlpatterns += router.urls
