from django.contrib import admin
from .models import Video,Comment
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id','title','owner','uploadtime')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','get_title','time','content')
    def get_title(self,obj):
        return obj.video.title
    get_title.admin_order_field = 'video__title'  
        
admin.site.register(Video,VideoAdmin)
admin.site.register(Comment,CommentAdmin)

