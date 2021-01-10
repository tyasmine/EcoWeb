from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("articles", views.articles_display, name="articles"),
    path("create", views.create, name="create"),
    path("create/<str:key>", views.create_object, name="create_object"),
    path("aboutus", views.about_us, name="aboutus"),
]