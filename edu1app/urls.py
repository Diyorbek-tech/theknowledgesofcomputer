from django.urls.conf import path
from .views import HomeClass,BlogClass

urlpatterns=[
    path('',HomeClass.as_view(),name='home'),
    path('blog/',BlogClass.as_view(),name='blog')
]