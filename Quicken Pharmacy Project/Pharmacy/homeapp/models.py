from django.db import models
class ProductDetails(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    price = models.IntegerField(max_length=10)
    brand = models.CharField(max_length=10,default='')
    def __str__(self):
        return ("Name : " + self.name + ",   Type : " + self.type + ",   Price : " + str(self.price) + ",   Brand : " + self.brand)

class Newsletter(models.Model):
    email = models.EmailField(max_length=50)
    def __str__(self):
        return ("Email : " + self.email)

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    def __str__(self):
        return ("Name : " + self.name + ", Subject : " + self.subject)

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return ("Username : " + self.username + ", Password : " + self.password)

class Registeration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=500)
    def __str__(self):
        return ("Name : " + self.name + ", Email : " + self.email + ", Username : " + self.username + ", Password : " + self.password)