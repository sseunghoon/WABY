from django.contrib import admin
from .models import Result, Question, Choice, Feedback

admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Feedback)
