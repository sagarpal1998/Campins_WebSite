from django import forms
from testapp.models import Project



class Project_form(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"