from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.UserList.as_view()),
    path('<int:pk>/',views.UserDetail.as_view()),
    # path()
]

urlpatterns = format_suffix_patterns(urlpatterns)