from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.EmailField()
    reg_date = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.email
