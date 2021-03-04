from django.conf.urls import url
from appthree import views


urlpatterns=[
    url(r'^$',views.users,name='users'),
]
