from django.contrib import admin

from Event.models import Session, Presentation, SessionComment, PresentationComment


class PresentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'session', 'is_verified']
    list_filter = ['session']


admin.site.register(Session)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(SessionComment)
admin.site.register(PresentationComment)
