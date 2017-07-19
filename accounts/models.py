from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                verbose_name=_('user'), related_name='my_profile')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    diagnosis_date = models.DateField(_('Date Diagnosed'), auto_now=False, auto_now_add=False, blank=True, null=True)
    d_type = models.IntegerField( blank=True, null=True)
    created = models.DateField(auto_now=True)