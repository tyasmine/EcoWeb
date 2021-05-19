from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Login Logout Register
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Presentation pages
    path("articles", views.articles_display, name="articles"),
    path("articles/<str:key>", views.articles_unique_display, name="articles_unique"),
    path("ideas", views.ideas_display, name="ideas"),
    path("projects", views.projects_display, name="projects"),
    path("portfolio", views.portfolio_display, name="portfolio"),
    path("products", views.products, name="products"),

    # Individual pages
    path("article/<str:key>", views.article, name="article"),
    path("idea/<str:key>", views.idea, name="idea"),
    path("project/<str:key>", views.project, name="project"),

    # Create
    path("create", views.create, name="create"),
    path("create_article", views.create_article, name="create_article"),
    path("create_project", views.create_project, name="create_project"),
    path("create_image", views.create_image, name="create_image"),
    path("create_idea", views.create_idea, name="create_idea"),

    #Command
    path("command", views.command, name="command"),

    # Else
    path("aboutus", views.about_us, name="aboutus"),
    path("credits", views.credits, name="credits"),
]