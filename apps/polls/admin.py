from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# admin.StackedInline 成行堆叠
# admin.TabularInline 列成表格
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', "questioner", 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['questioner']}),
    ]
    inlines = [ChoiceInline]
    # 列表显示字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 列表筛选
    list_filter = ['pub_date']
    # 添加列表查询条件
    search_fields = ['question_text']


# 修改admin 默认的项目名称
admin.site.site_header = '投票站点管理界面'
# 修改admin 默认的标签页显示的标题
admin.site.site_title = '投票管理'
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
