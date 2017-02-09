from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^test/$', views.test, name='test'),
    url(r'^chaincode/$', views.chaincode, name='chaincode'),
    url(r'^script2.js/$', views.test2, name='test2'),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^animal/$', views.animal, name='animal'),
]
