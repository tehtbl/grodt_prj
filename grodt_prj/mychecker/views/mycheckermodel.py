from django.contrib.auth import mixins as auth_mixins
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from ..forms import MyCheckerModelFormGeneral
from ..models import MyCheckerModel


class MyCheckerModelCreateView(auth_mixins.PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = MyCheckerModel
    form_class = MyCheckerModelFormGeneral
    permission_required = "mychecker.add_mycheckermodel"
    template_name = "mychecker/mycheckermodel/form.html"
    success_url = reverse_lazy("mychecker:mycheckermodels_list")
    success_message = "%(name)s was created successfully"


class MyCheckerModelUpdateView(auth_mixins.PermissionRequiredMixin, UpdateView):
    model = MyCheckerModel
    form_class = MyCheckerModelFormGeneral
    permission_required = "mychecker.edit_mycheckermodel"
    template_name = "mychecker/mycheckermodel/form.html"
    success_url = reverse_lazy("mychecker:mycheckermodels_list")
    pk_url_kwarg = 'uuidpk'


class MyCheckerModelDeleteView(auth_mixins.PermissionRequiredMixin, DeleteView):
    model = MyCheckerModel
    permission_required = "mychecker.del_mycheckermodel"
    success_url = reverse_lazy("mychecker:mycheckermodels_list")
    pk_url_kwarg = 'uuidpk'

    # Now, there's no ``confirmation is required'' anymore!
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MyCheckerModelDetailView(auth_mixins.PermissionRequiredMixin, generic.DetailView):
    model = MyCheckerModel
    permission_required = "mychecker.view_mycheckermodel"
    template_name = "mychecker/mycheckermodel/detail.html"
    pk_url_kwarg = 'uuidpk'


class MyCheckerModelListView(auth_mixins.PermissionRequiredMixin, ListView):
    model = MyCheckerModel
    permission_required = "mychecker.view_mycheckermodel"
    template_name = "mychecker/mycheckermodel/list.html"
    context_object_name = "my_mycheckermodels"
