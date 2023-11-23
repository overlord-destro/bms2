from django.db import models
import datetime
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    pub_year = models.CharField(max_length=4)

    def __str__(self):
        return self.title


class Accessor(models.Model):
    book_title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    mail = models.EmailField(default="")
    date_checked_out = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name