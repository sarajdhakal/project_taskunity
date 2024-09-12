from django.contrib import admin

from .models.kanban import (Issue)
from .models.kanban import Comment

# Register your models here.

admin.site.register(Issue)
admin.site.register(Comment)
