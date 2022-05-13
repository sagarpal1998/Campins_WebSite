from django.db import models


gender_choice = (
    ('Male','Male'),
    ('Female','Female'),
    ('Transgender','Transgender')
)
class Possition(models.Model):
    tittel = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tittel
        

# Create your models here.
class Project(models.Model):
    f_name = models.CharField(max_length=15)
    m_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=15,choices=gender_choice,null=True)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    place = models.ForeignKey(Possition,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    date1 = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.f_name
        