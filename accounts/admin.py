from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question, Choice, Book
from django import forms

class BookAdminForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise forms.ValidationError(
                'Django入れて！',
            )
        return title
        
@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'price')
    ordering = ('-price',)
    fields = ('title', 'image', 'price')
    form = BookAdminForm

admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(Book, BookModelAdmin)
# admin.site.register(CustomUser)