from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
STATE_CHOICES =( 

    ("AP","Andhra Pradesh"),
    ("AR","Arunachal Pradesh"),
    ("MN","Manipur"),
    ("ML","Meghalaya"),
    ("MZ","Mizoram"),
    ("NL","Nagaland"),
    ("OR","Odisha"),
    ("PB","Punjab"),
    ("RJ","Rajasthan"),
    ("SK","Sikkim"),
    ("TN","Tamil Nadu"),
    ("TG","Telangana"),
    ("TR","Tripura"),
    ("UT","Uttarakhand"),
    ("UP","Uttar Pradesh"),
    ("WB","West Bengal"),
    ("AN","Andaman and Nicobar Islands"),
    ("CH","Chandigarh"),
    ("DN","Dadra and Nagar Haveli"),
    ("DD","Daman and Diu"),
    ("DL","Delhi"),
    ("LD","Lakshadweep"),
    ("PY","Puducherry"), 
    
) 
class Resume(models.Model):
    name=models.CharField(max_length=80)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=STATE_CHOICES,max_length=80)
    gender=models.CharField(max_length=50)
    location=models.CharField(max_length=100)
    pimage=models.ImageField(upload_to='pimage',blank=True)
    rdoc=models.FileField(upload_to='rdoc',blank=True)





