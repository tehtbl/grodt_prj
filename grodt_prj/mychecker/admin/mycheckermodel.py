from core import constants as core_const
from django.contrib import admin


class MyCheckerModelAdmin(admin.ModelAdmin):
    exclude = core_const.LIST_MODEL_FIELD_EXCLUDES
