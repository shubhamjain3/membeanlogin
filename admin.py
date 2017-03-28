from django.contrib import admin
from quiz.models import quiz
class quizadmin(admin.ModelAdmin):
    list_display=['exam','s_no','ans']
    class Meta:
        model=quiz
admin.site.register(quiz,quizadmin)
