from django.conf.urls import url
from .forms import CustomEditProfileForm

urlpatterns = [
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$', {'edit_profile_form': CustomEditProfileForm, },
        name='userena_profile_edit')

]