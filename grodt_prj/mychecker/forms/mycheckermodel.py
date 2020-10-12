from core import constants as core_const
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Submit
from django import forms

from ..models import MyCheckerModel


class MyCheckerModelFormGeneral(forms.ModelForm):

    class Meta:
        model = MyCheckerModel
        exclude = core_const.LIST_MODEL_FIELD_EXCLUDES

    def __init__(self, *args, **kwargs):
        super(MyCheckerModelFormGeneral, self).__init__(*args, **kwargs)

        # self.fields["domain"].required = False

        self.helper = FormHelper()
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "form-label col-3 col-form-label"
        self.helper.field_class = "col"

        self.helper.layout = Layout(
            *self.fields,
            Div(
                Submit("save", "Save Changes"),
                css_class="form-footer",
            )
        )
