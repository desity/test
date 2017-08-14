from django.contrib import admin
from .models import Applicant, Test, Tquestion, User
from django.utils.translation import ugettext_lazy as _


class MarkListFilter(admin.SimpleListFilter):
    title = _('SCORED MARK PASS')
    parameter_name = 'mark_pass'

    def lookups(self, request, model_admin):
        array1 = {
                   ('0-10',  _('0-10')),
                   ('10-20', _('10-20')),
                   ('20-30', _('20-30')),
                   ('30-40', _('30-40')),
                   ('40-50', _('40-50')),
                   ('50-60', _('50-60')),
                   ('60-70', _('60-70')),
                   ('70-80', _('70-80')),
                   ('80-90', _('80-90')),
                   ('90-100', _('90-100'))
        }
        array1 = sorted(array1)
        return array1

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == '0-10':
                return queryset.filter(mark_pass__lte=10, mark_pass__gte=0)
            if self.value() == '10-20':
                return queryset.filter(mark_pass__lte=20, mark_pass__gte=10)
            if self.value() == '20-30':
                return queryset.filter(mark_pass__lte=30, mark_pass__gte=20)
            if self.value() == '30-40':
                return queryset.filter(mark_pass__lte=40, mark_pass__gte=30)
            if self.value() == '40-50':
                return queryset.filter(mark_pass__lte=50, mark_pass__gte=40)
            if self.value() == '50-60':
                return queryset.filter(mark_pass__lte=60, mark_pass__gte=50)
            if self.value() == '60-70':
                return queryset.filter(mark_pass__lte=70, mark_pass__gte=60)
            if self.value() == '70-80':
                return queryset.filter(mark_pass__lte=80, mark_pass__gte=70)
            if self.value() == '80-90':
                return queryset.filter(mark_pass__lte=90, mark_pass__gte=80)
            if self.value() == '90-100':
                return queryset.filter(mark_pass__lte=100, mark_pass__gte=90)
        else:
            return queryset


class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('email', 'passing_date', 'test_status', 'mark_pass', 'status_description', 'qquery')
    search_fields = ('email', 'name', 'surname')
    list_filter = ('passing_date', 'startpassing_date', 'test_status', MarkListFilter)
    date_hierarchy = 'passing_date'


class TquestionAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'question', 'choicer1', 'choicer2', 'choicer3', 'choicer4', 'choicer5')
    fields = ('test_name',
              'question',
              ('choice1', 'choicer1'),
              ('choice2', 'choicer2'),
              ('choice3', 'choicer3'),
              ('choice4', 'choicer4'),
              ('choice5', 'choicer5'))


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'q_count', 'test_descr', 'submit_if_leave', 'timetest')
    search_fields = ('test_name', 'test_descr')


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'surname', 'password', 'regdate', 'veryfied', 'active', 'comment')


admin.site.register(Applicant, ApplicantAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Tquestion, TquestionAdmin)
admin.site.register(User, UserAdmin)
