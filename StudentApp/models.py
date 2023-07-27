from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"


class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city_name}"

class Student2(models.Model):
    Stud_name = models.CharField(max_length=50)
    Stud_phno = models.BigIntegerField()
    Stud_email = models.CharField(max_length=100)
    Stud_city = models.ForeignKey(City,on_delete=models.CASCADE)#when we delete parent table data then the related child data will aslo delete
    Stud_course = models.ForeignKey(Course,on_delete=models.CASCADE)
    Stud_fees = models.IntegerField()