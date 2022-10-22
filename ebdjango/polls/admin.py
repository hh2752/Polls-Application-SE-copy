# from django.contrib import admin

from .models import Question, Choice
from django.contrib import admin

from .models import Question
# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
# admin.site.register(Choice)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)