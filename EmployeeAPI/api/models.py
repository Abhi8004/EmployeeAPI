from django.db import models

# Create your models here.

#Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    Qualification = models.CharField(max_length=500)
    Qualification_name = models.CharField(max_length=500)
    Project_Name = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Description = models.TextField()
    from_date = models.DateTimeField(auto_now=True)
    to_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name + '--' + self.address
    
#Employee Model
class Employee(models.Model):
        name = models.CharField(max_length=500)
        email = models.CharField(max_length=500)
        age = models.CharField(max_length=500)
        gender = models.CharField(max_length=500,choices=(('M','M'),('F','F')))
        phone = models.CharField(max_length=500)
        address = models.CharField(max_length=500)
        HouseNo = models.CharField(max_length=500)
        street = models.CharField(max_length=500)
        city = models.CharField(max_length=500)
        state = models.CharField(max_length=500)
        about = models.TextField()

        company=models.ForeignKey(Company, on_delete=models.CASCADE)
