from django.contrib import admin

from .models import Category, ChoiceQuestion


class ChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ['content', 'category', 'created_time']
    fields = ['content', 'category', 'option_a', 'option_b', 'option_c', 'option_d', 'answer', 'solution']


admin.site.register(Category)
admin.site.register(ChoiceQuestion)
