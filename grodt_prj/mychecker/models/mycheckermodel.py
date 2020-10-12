from core.models import MyAbstractModelObject
from django.db import models
from django.utils.encoding import smart_text
from django.utils.translation import gettext_lazy as _
from users.models import MyUser


class MyCheckerModel(MyAbstractModelObject):

    name = models.CharField(_("Name"), max_length=100, unique=True)

    prvkey = models.CharField(_("Private Key"), max_length=65)
    pubkey = models.CharField(_("Public Key"), max_length=42)
    balance = models.FloatField(_("Balance"))

    class Meta:
        ordering = ["name"]
        app_label = "mychecker"
        verbose_name = _("MyCheckerModel")
        verbose_name_plural = _("MyCheckerModels")

    def __init__(self, *args, **kwargs):
        super(MyCheckerModel, self).__init__(*args, **kwargs)

    @property
    def tags(self):
        return [
            {
                "name": self.balance,
                "label": self.balance,
                "type": "tag-item",
                "color": "warning"  # TODO
            }
        ]

    @property
    def admins(self):
        """Return the administrators of this Model.

        :return: a list of User objects
        """

        return MyUser.objects.filter(
            is_superuser=False,
            objectaccess__content_type__model="mycheckermodel",
            objectaccess__object_id=self.pk
        )

    def __str__(self):
        return smart_text(self.name)
