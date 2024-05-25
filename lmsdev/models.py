from django.db import models

from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser

#all models get an auto index primary key
#python manage.py makemigrations
#python manage.py migrate
#make changes to admin.py

class allEdits(models.Model):
    slug: models.CharField(max_length=50)

    class Meta:
        abstract = True

# django.contrib.auth already provides a comprehensive user class
# in order to use our extended version with django's built in authentication system
# we added this line to settings.py
# AUTH_USER_MODEL = "lmsdev.user"
class user(AbstractUser, allEdits):
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.email


class tag(allEdits):
    text = models.CharField(max_length=50 ,null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.text

class question_type(allEdits):
    text = models.CharField(max_length=50 ,null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.text

class response_option(allEdits):
    text = models.CharField(max_length=50 ,null=True)
    is_correct = models.BooleanField()
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.text

class question(allEdits):
    title = models.CharField(max_length=50, null=True)
    prompt = models.TextField(blank=False, null=False)
    response_when_correct = models.CharField(max_length=50, blank=True, null=True)
    response_when_incorrect = models.CharField(max_length=50, blank=True, null=True)
    manual_grade = models.BooleanField(default=False)
    question_type = models.ForeignKey(question_type, on_delete=models.SET_NULL, related_name="questions", null=True)
    tags = models.ManyToManyField(tag)
    response_options = models.ManyToManyField(response_option)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title


class quiz(allEdits):
    title = models.CharField(max_length=50, null=True)
    tags = models.ManyToManyField(tag)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title


class quiz_version(quiz):
    version = models.FloatField(null=True)
    startDate = models.DateTimeField(null=True)
    endDate = models.DateTimeField(null=True)
    questions = models.ManyToManyField(question)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.version


class department(allEdits):
    title = models.CharField(max_length=50, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title


class block(allEdits):
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title


class page(allEdits):
    title = models.CharField(max_length=50, blank=True, null=True)
    blocks = models.ManyToManyField(block)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title


class course(allEdits):
    title = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(department, on_delete=models.SET_NULL, related_name="courses", null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title

class section(allEdits):
    course = models.ForeignKey(course, on_delete=models.SET_NULL, related_name="sections", null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)
    term = models.CharField(max_length=20, blank=True, null=True)
    pages = models.ManyToManyField(page)
    teachers = models.ManyToManyField(user, related_name="teachers")
    students = models.ManyToManyField(user, related_name="students")
    assistants = models.ManyToManyField(user, related_name="assistants")
    observers = models.ManyToManyField(user, related_name="obervers")
    history = HistoricalRecords()

    def __str__(self) -> str:
        return self.title
