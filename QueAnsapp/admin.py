from django.contrib import admin

# Register your models here.

from .models import Post,Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','question','slug','author','image','answer','created','modified','status']
    list_editable = ['status']
    search_fields = ['question','answer']
    # date_hierarchy = ['created']





admin.site.register(Post,PostAdmin)
