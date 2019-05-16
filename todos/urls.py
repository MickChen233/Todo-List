from django.conf.urls import url,include

from .import views
from rest_framework import routers
from .api import TodoViewSet


router = routers.DefaultRouter()
router.register(r'todos',TodoViewSet,'todos')

urlpatterns = [
    url(r'^api/',include(router.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details,name='details'),
    url(r'^add', views.add, name='add'),
    url(r'^delete/(?P<id>\w{0,50})/$', views.delete, name='delete')
    
]




