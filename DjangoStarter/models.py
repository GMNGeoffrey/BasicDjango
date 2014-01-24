from django.db import models
#from django.forms import * #Used to make Django forms.
#from django.contrib.auth.models import User #IE: Import Django's User object.



#This is a basic Django Model with one "field."
class Family(models.Model):
 surname = models.CharField(max_length=60)





#This is a more complex Django Model with many "fields."
class Family_Member(models.Model):
 #The following is a basic Text Field. The max_length is required.
 email = models.CharField(max_length=75)

 #Defaults can also be applied in most Model Fields.
 allergies = models.CharField(max_length=50,default="No allergies!")

 #Django's Model Fields can get sufficiently complex, too -- for example:
 name = models.CharField(max_length=200, unique=True, error_messages={'unique':"This name is already taken by someone else!"})

 #Following is a simple example of how to "link" an object to another.
 #This concept is called a "Foreign Key."
 family = models.ForeignKey(Family)





#Django's ORM allows us to filter and query the database while opaquely
# hiding the database-specific queries that are going on behind-the-scene.
# Thus, we can call on our database as if it were just a Python object! 

#For example, we can grab all of the Family rows in the database...
all_families = Family.objects.all()

#Or only the "Smith" family.
smith = Family.objects.filter(surname="Smith")

#Or the Family to the first Family_Member in the database.
first_family = Family_Member.objects.first().family
#Note that this is the same as:
first_family = getattr(Family_member.objects.first(), "family")
#or...
first_family_member = Family_member.objects.first()
first_family = first_family_member.family



