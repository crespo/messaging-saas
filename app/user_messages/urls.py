from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserMessageList.as_view(), name=views.UserMessageList.name),
    path('<uuid:pk>', views.UserMessageDetail.as_view(), name=views.UserMessageDetail.name),
]