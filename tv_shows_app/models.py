from django.db import models
import datetime

# Create your models here.
class ShowManager(models.Manager):
    #validator for the /create path
    def create_validator(self,postData):
        errors= {}
        today = str(datetime.date.today())
        match = Show.objects.filter(title=postData['title'])
        if len(postData['title']) < 2:
            errors['name'] = "Show title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters"
        if len(postData['description']) < 10:
            if len(postData['description']) >0:
                errors['description'] = "Description must be greater than 10 charaters or left blank"
        if postData['release_date'] >= today:
            errors['reelease_date'] = "Release date must be in the past"
        if len(match) > 0:
            errors['exists'] = "This show already exists"
        return errors
    
    def update_validator(self, postData):
        errors= {}
        today = str(datetime.date.today())
        if len(postData['title']) < 2:
            errors['name'] = "Show title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must be at least 3 characters"
        if len(postData['description']) < 10:
            if len(postData['description']) >0:
                errors['description'] = "Description must be greater than 10 charaters or left blank"
        if postData['release_date'] >= today:
            errors['reelease_date'] = "Release date must be in the past"
        return errors




class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # overriding .manager
    objects= ShowManager()
