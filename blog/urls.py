from blog import views
from django.urls import path, include


urlpatterns = [
    #path("",views.hello),
    #path("login/<name>/", views.login),
    #path("details/<name>/<int:age>/<city>/", views.details),
    path("",views.index),
    path("about/", views.about),
    path("blog/", views.blog),
    path("contact/", views.contact),
    path("features/", views.features),
    path("login/", views.login),
    path("signup/", views.signup),

    path("aftersignup/", views.AfterSignup.as_view()),
    path("afterlogin/", views.AfterLogin.as_view()),
    path("checkotp/", views.Checkotp.as_view()),
    path('logout/', views.logout),
    path("addblog/",views.addblog),

    path("blogdata/", include('blogdata.urls')),


]


