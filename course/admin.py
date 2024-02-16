from django.contrib import admin
from . import models as m

admin.site.register(m.Course)
admin.site.register(m.UserCourse)
