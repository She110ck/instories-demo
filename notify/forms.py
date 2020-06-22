from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django import forms,

from notify.models import Push


class PushForm(forms.ModelForm):
    class Meta:
        model = Push
        fields = ['title', 'text', 'create_date', 'send_date', ]

    def __init__(self, *args, **kwargs):
        super(PushForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    # _('Basic information'),
                    Field('title', wrapper_class="col-md-6"),
                    Field('text', wrapper_class="col-md-6"),
                    Field('create_date', wrapper_class="col-md-12"),
                ),
                Tab(
                    # _('Other information'),
                    Field('image', wrapper_class="col-md-6"),
                    Field('cropping', wrapper_class="col-md-6"),
                    Field('cif', wrapper_class="col-md-6"),
                    Field('slug', wrapper_class="col-md-6")
                )
            )
        )
