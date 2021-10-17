from django.contrib import admin
from .models import Post


#actions
def Do_publish(modeladmin,request,queryset):
    number = queryset.update(status = 'p')
    if number == 1 :
        message = "Article"
    else:
        message = "Articles"

    modeladmin.message_user(request,f"{message} published")
Do_publish.short_description = "Publish article(s)"

def Do_draft(modeladmin,request,queryset):
    number = queryset.update(status = 'd')
    if number == 1 :
        message = "Article"
    else:
        message = "Articles"

    modeladmin.message_user(request,f"{message} drafted")
Do_draft.short_description = "Draft article(s)"


#Post Admin Panel
class AdminPost(admin.ModelAdmin):
    list_display = ('title','description_shorter','image_show','author','created','status')
    list_filter  = ('created','status','author')
    search_fields= ('title','description',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    actions = (Do_publish,Do_draft,)

admin.site.register(Post,AdminPost)