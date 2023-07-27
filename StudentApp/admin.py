from django.contrib import admin

from StudentApp.models import Course, City, Student2

# Register your models here.
admin.site.register(Course)#it is used to register to admin panel
admin.site.register(City)
admin.site.register(Student2)



