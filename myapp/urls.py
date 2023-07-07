from django.urls import path
from . import views


urlpatterns = [
    path("",views.Index,name="apphome"),
    path("about/",views.About,name="about"),
    path("contactus/",views.contact,name="contact"),
    path("services/",views.Services,name="services"),
    path("myapp/viewproduct/<int:id>", views.ViewProduct, name="viewproduct"),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/blogpost/<int:id>/', views.blog_post, name='blog_post'),
    path('signup/', views.Signup, name='signup'),
    path('signup_user/', views.Signup_user, name='signup_user'),
    path('verify/', views.Verify, name='verify'),
    path('login/', views.Login, name='login'),
    path('login_user/', views.Login_user, name='login_user'),
    path("logout/",views.Logout,name='logout'),
    
]
