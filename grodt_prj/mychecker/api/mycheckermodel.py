from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from ..models import MyCheckerModel
from ..serializers import MyCheckerModelSerializer


class MyCheckerModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
    serializer_class = MyCheckerModelSerializer

    def get_queryset(self):
        """Filter queryset based on current user."""
        return MyCheckerModel.objects.get_for_admin(self.request.user)

    def perform_destroy(self, instance):
        """Add custom args to delete call."""
        instance.delete(self.request.user)
