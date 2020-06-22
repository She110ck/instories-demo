from django.contrib import admin

# Register your models here.
from notify.models import Option, Push


class OptionsAdmin(admin.ModelAdmin):
    pass


class PushesAdmin(admin.ModelAdmin):
    list_display = ('title', 'count',)
    list_display_links = ('title',)
    pass


admin.site.register(Option, OptionsAdmin)
admin.site.register(Push, PushesAdmin)
