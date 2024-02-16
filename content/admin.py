from django.contrib import admin

from . import models as m

admin.site.register(m.Book)
admin.site.register(m.Word)
admin.site.register(m.Sentence)
admin.site.register(m.Dictation)
admin.site.register(m.Grammar)
