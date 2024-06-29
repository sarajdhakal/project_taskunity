from django.contrib import admin

from .models.kanban import (Issue)

# Register your models here.

admin.site.register(Issue)