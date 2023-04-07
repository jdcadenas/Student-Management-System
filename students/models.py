from django.db import models

# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField( max_length=50)
  last_name = models.CharField( max_length=50)
  email= models.EmailField( max_length=100)
  field_study=models.CharField(max_length=50)
  gpa = models.FloatField()
  
  class Meta:
        '''Meta definition for Student.'''
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

  def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
  