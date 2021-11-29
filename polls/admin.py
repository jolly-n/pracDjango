from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline): # TabularInline을 사용해 테이블 기반 형식으로 표시
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [  # 필드를 묶어서 제목을 준다
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # question페이지 안에서 choice를 관리할 수 있도록 한다.

    list_filter = ['pub_date']  # 발행일을 기준으로 필터링 할 수 있는 기능 제공
    search_fields = ['question_text']  # 검색창 기능 제공

admin.site.register(Question, QuestionAdmin)