from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(CustomUser)