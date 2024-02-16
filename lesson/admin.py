from django.contrib import admin
from . import models as m

admin.site.register(m.Lesson)
admin.site.register(m.UserLesson)
admin.site.register(m.Question)
admin.site.register(m.Example)
