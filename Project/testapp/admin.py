from pyexpat import model
from django.contrib import admin
from testapp import models
from testapp.models import Possition
from testapp.models import Project


# Register your models here.
admin.site.register(Project)
admin.site.register(Possition)