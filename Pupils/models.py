from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    month = models.CharField(max_length=20)
    grade = models.IntegerField()
