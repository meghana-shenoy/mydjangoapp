from django.db import models

class Contact(models.Model):  
    firstname = models.CharField(max_length=100)  
    lastname = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)  
    mobile = models.IntegerField()  
    age = models.IntegerField()  
    
    def __str__(self):
        return self.firstname
    class Meta:  
        db_table = "contact"

