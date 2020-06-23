from adminlteui.admin import ImageBox
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
from django import forms
from image_cropping import ImageCropWidget
from easy_thumbnails.fields import ThumbnailerImageField

import cruds_adminlte

from notify.models import Push


class PushForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/notify/send/'
        self.helper.add_input(Submit('submit', 'Отправить'))

    def clean(self):
        super().clean()

    class Meta:
        model = Push
        fields = ['title', 'text', 'image', 'send_date', 'name']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': ' Укажите заголовок'}),
            'text': forms.Textarea(attrs={'placeholder': ' Введите текст уведомления', 'rows': 4}),
            'image': ImageCropWidget(),
            'send_date': forms.DateInput(attrs={'placeholder': 'DD/MM/YY'}, format='%d/%m/%y')
        }

# class PushForm(forms.Form):
#     title = forms.CharField(widget=, max_length=50,
#                             label='Заголовок уведомления', required=False)
#     text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': ' Введите текст уведомления', 'rows': 4}),
#                            label='Текст уведомления', required=False)
#     image = forms.ImageField(widget=ImageCropWidget(), required=False)
#     send_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YY'}), label='Дата отправки',
#                                 required=False)
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-6'}), label='Название уведомления',
#                            required=False)
#
# def image_thumb(self):
#     return '<img src="/media/%s" height="100" />' % self.image
