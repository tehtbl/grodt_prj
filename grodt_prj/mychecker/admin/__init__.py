from django.contrib import admin

from ..models import MyCheckerModel
from .mycheckermodel import MyCheckerModelAdmin

admin.site.register(MyCheckerModel, MyCheckerModelAdmin)
