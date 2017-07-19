from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import EditProfileForm

class CustomEditProfileForm(EditProfileForm):
    d_type = forms.IntegerField(label = (u'Diabetes Type'))

    date_diag = forms.DateField(label=_(u'Diagnosis Date'),
                                 required=False)


    def save(self):
        user = super(CustomEditProfileForm, self).save()
        user_profile = user.get_profile()
