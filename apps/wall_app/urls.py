from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_message', views.PostMessage),
    path('delete_message', views.DeleteMessage),
    path('post_comment', views.PostComment),
    path('delete_comment', views.DeleteComment),
]


# urlpatterns = [
#     path('', views.Login_Reg),
#     path('register', views.Register),
#     path('login', views.Login),
#     path('success', views.Success),
#     path('logout', views.Logout)
# ]