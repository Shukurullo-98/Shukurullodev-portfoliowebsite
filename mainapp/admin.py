from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)
    fields = (
        'title', 'description',
    )


admin.site.register(Portfolio)
admin.site.register(AboutPage)
admin.site.register(Blog, PostAdmin)

# Register your models here.
