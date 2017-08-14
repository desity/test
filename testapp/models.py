from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import pytz
import datetime



class Applicant(models.Model):
    test_id = models.IntegerField(default=0)
    test_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    passing_date = models.DateTimeField(default=timezone.now)
    mark_pass = models.IntegerField(default=0)
    test_status = models.CharField(max_length=50)
    startpassing_date = models.DateTimeField(default=timezone.now)
    qquery = models.TextField(default="")
    status_description = models.CharField(max_length=50)



    def publish(self):
        self.passing_date = timezone.now()
        self.save()

    def __str__(self):
        return self.surname


class Tquestion(models.Model):
    test_name = models.ForeignKey('Test')
    question = models.TextField(null=True)
    choice1 = models.CharField(max_length=200)
    choicer1 = models.BooleanField()
    choice2 = models.CharField(max_length=200)
    choicer2 = models.BooleanField()
    choice3 = models.CharField(max_length=200)
    choicer3 = models.BooleanField()
    choice4 = models.CharField(max_length=200)
    choicer4 = models.BooleanField()
    choice5 = models.CharField(max_length=200)
    choicer5 = models.BooleanField()

    def __str__(self):
        return self.test_name.__str__() + '  -  ' + self.question


class Test(models.Model):
    test_name = models.CharField(max_length=50, unique=True)
    q_count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    test_descr = models.CharField(max_length=200)
    submit_if_leave = models.BooleanField(default='False')
    timetest = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.test_name


class User(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    regdate = models.DateTimeField(default=timezone.now)
    veryfied = models.BooleanField(default='False')
    active = models.BooleanField(default='False')
    activatecode = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
"""
class Tquestion(models.Model):
    test_name = models.ForeignKey('Test')
    question = models.TextField(blank=True, null=True)
    choice1 = models.CharField(max_length=200)
    choicer1 = models.BooleanField(default='False')
    choice2 = models.CharField(max_length=200)
    choicer2 = models.BooleanField(default='False')
    choice3 = models.CharField(max_length=200)
    choicer3 = models.BooleanField(default='False')
    choice4 = models.CharField(max_length=200)
    choicer4 = models.BooleanField(default='False')
    choice5 = models.CharField(max_length=200)
    choicer5 = models.BooleanField(default='False')

    def __str__(self):
        return self.test_name.__str__() + '  -  ' + self.question
"""
"""class SubmitTestForm(ModelForm):
    class Meta:
        model = Tquestion
        fields = ['Question', 'Choicer1', 'Choicer2', 'Choicer3', 'Choicer4', 'Choicer5']"""
