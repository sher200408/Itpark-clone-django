from django.contrib import admin
from .models import Profil,Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']

admin.site.register(Profil)
admin.site.register(Skill, SkillAdmin)