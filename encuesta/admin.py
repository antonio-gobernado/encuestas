from django.contrib import admin

# Register your models here.

from .models import Poll, Sig, Mejora, Covid

admin.site.register(Poll)
admin.site.register(Sig)
admin.site.register(Mejora)
admin.site.register(Covid)