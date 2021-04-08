from django.contrib import admin
from .models import User, Comment_Idea, Comment_Article, Article, Idea, Project, Comment_Project, Image, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Comment_Article)
admin.site.register(Comment_Idea)
admin.site.register(Article)
admin.site.register(Idea)
admin.site.register(Project)
admin.site.register(Comment_Project)
admin.site.register(Image)