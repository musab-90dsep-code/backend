

from django.contrib import admin
from .models import Content, InstitutionStats, Notice, News, Teacher, Video, Event

admin.site.register(Content)
admin.site.register(Notice)
admin.site.register(News)
admin.site.register(Video)
admin.site.register(InstitutionStats)
admin.site.register(Teacher)
admin.site.register(Event)