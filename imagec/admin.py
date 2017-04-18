from django.contrib import admin

from .models import profile,Post,Album
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = profile
admin.site.register(profile, profileAdmin)

admin.site.register(Post)
admin.site.register(Album)