from core import constants as core_const
from rest_framework import serializers

from ..models import MyCheckerModel


class MyCheckerModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyCheckerModel
        exclude = core_const.LIST_MODEL_FIELD_EXCLUDES

    def validate_name(self, value):
        """Check name constraints."""
        value = value.lower()
        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        """Set permissions."""
        mycheckermodel = MyCheckerModel(**validated_data)
        creator = self.context["request"].user

        mycheckermodel.save(creator=creator)

        return mycheckermodel
