from django.contrib import admin
from .models import profileDetail, Title, Question, Answer, ok_Answer
# Register your models here.
@admin.register(profileDetail)
class profDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'date_of_birth', 'email', 'region')

@admin.register(Title)
class titleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Question)
class queAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'question')

@admin.register(Answer)
class ansAdmin(admin.ModelAdmin):
    list_display = ('question', 'id', 'answer')

@admin.register(ok_Answer)
class ok_ansAdmin(admin.ModelAdmin):
    list_display = ('question', 'ok_answer')

