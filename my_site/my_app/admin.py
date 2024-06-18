from django.contrib import admin
from modeltranslation.translator import TranslationOptions,register
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Story)
admin.site.register(Group)

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('user',)




@admin.register(Post)
class PostAdmin(TranslationAdmin):

    group_fieldsets = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
