from django.contrib import admin
from .models import Question, Choice

from django.db.models import Sum


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    def justas_choice_count(self, obj):
        return obj.choice_set.count()

    def justas_activity(self,obj):
        return obj.choice_set.aggregate(Sum('votes'))['votes__sum'] or 0
        #return obj.choice_set.count()


    list_display = ('question_text', 'pub_date','was_published_recently', 'justas_choice_count', 'justas_activity')
    list_filter = ['pub_date']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


admin.site.register(Choice)

# Register your models here.
