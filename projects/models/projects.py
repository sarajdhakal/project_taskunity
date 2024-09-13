from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    Stauts = {
        "Private": "Private",
        "Public": "Public",
        "Team": "Team"
    }
    status = models.CharField(
        max_length=100,
        choices= Stauts,
        default="Private"
          )
    Progress={
        "Not started": "Not Started",
        "Completed": "Completed",
        "In Progress": "In Progress",
        "Delivered" : "Delivered",

        }
    progress = models.CharField(
        max_length=100,
        choices=Progress,
        default='Not Started',
    )
    # user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    image = models.ImageField(upload_to='uploadimages/projects/', default='p1.jpg')
    users = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True)
    extended_date = models.DateField(null=True)
    team_member = models.ManyToManyField(User,related_name='projects')
    attachments = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
    
    