from django.db import models


class AccessRequirment(models.TextChoices):
    ANYONE = "any" , "Anyone" 
    EMAIL_REQUIRED = "mail" , "Email Required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "publish" , "published"
    COMING_SOON = "soon" , "Coming Soon"
    DRAFT = "draft" , "Draft"


def handle_upload(instance , filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to=handle_upload , null=True , blank=True)
    access = models.CharField(
                              max_length=15 , 
                              choices=AccessRequirment.choices ,
                              default=AccessRequirment.EMAIL_REQUIRED
                              ) 
    status = models.CharField(
                              max_length=15 , 
                              choices=PublishStatus.choices ,
                              default=PublishStatus.DRAFT 
                              )
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    
