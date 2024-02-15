from django.contrib import admin
from . import models as m

admin.site.register(m.Task)
admin.site.register(m.Example)
