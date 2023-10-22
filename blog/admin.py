from django.contrib import admin
from blog.models import Post , Category , Comment
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Post)
admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display =('name','post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ['name','post']
    
admin.site.register(Comment,CommentAdmin)
# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','author','counted_views','status','published_date','created_date')
    list_filter=('author',)
    #ordering=['-created_date']
    search_fields=['title','content']
    summernote_fields=('content',)