
from django.urls import path, include
from blogdata import  views

urlpatterns = [

    path("afteraddblog/",views.BlogAdd.as_view()),
    path("allblog/", views.allblog),
    path("myblog/", views.myblog),

]
