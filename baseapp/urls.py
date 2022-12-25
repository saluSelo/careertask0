from django.urls import path, include 
from baseapp import views 
 
urlpatterns = [ 
     path('baseapp/get', views.post_list),
     path('baseapp/post', views.add_post),
]