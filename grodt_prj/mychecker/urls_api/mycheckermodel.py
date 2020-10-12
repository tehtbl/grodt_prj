from rest_framework import routers

from .. import api

router = routers.SimpleRouter()
router.register(r"mycheckermodels", api.MyCheckerModelViewSet, basename="mycheckermodel")

urlpatterns_mycheckermodel = router.urls
