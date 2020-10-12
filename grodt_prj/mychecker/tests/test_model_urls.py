import pytest
from django.urls import reverse_lazy

pytestmark = pytest.mark.django_db


def test_urls_mychecker_index():
    assert reverse_lazy("mychecker:index") == "/mychecker/"


def test_urls_mychecker_mycheckermodel_list():
    assert reverse_lazy("mychecker:mycheckermodels_list") == "/mychecker/mycheckermodels/"
