from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

# __________________________________________________________   
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Foreign Key to Author

    def __str__(self):
        return self.title

  


#___________________________________________________________________


from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title  # ✅ Display course title properly

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)  # ✅ Many-to-Many relationship

    def __str__(self):
        return self.student_name  # ✅ Display student name properly

#_________________________________________________________



from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name