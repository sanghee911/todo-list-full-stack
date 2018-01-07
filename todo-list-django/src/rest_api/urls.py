from django.conf.urls import url
from rest_api.views import ToDoList, ToDoDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^todo-list/$', ToDoList.as_view(), name='todo-list'),
    url(r'^todo-list/(?P<pk>[0-9]+)/$', ToDoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)