from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(category)


# Register your models here.


#class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ['user' , 'avatar' , 'description']

#admin.site.register(UserProfile, UserProfileAdmin)


#class ArticleAdmin(admin.ModelAdmin):
    #search_fields = ['title' , 'content']
    #list_display = ['title' , 'category' , 'created_at']

#admin.site.register(Article,ArticleAdmin)