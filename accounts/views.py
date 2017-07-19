# from django.core.urlresolvers import reverse
# from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth import get_user_model
# from django.contrib import messages
# from django.utils.translation import ugettext as _
# from userena.decorators import secure_required
# from userena.utils import get_profile_model, get_user_profile
# from userena import signals as userena_signals
# from userena import settings as userena_settings
# from guardian.decorators import permission_required_or_403
# from django.views.generic import TemplateView
# from .models import MyProfile
#
# class ExtraContextTemplateView(TemplateView):
#     """ Add extra context to a simple template view """
#     extra_context = None
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
#         if self.extra_context:
#             context.update(self.extra_context)
#         return context
#
#     # this view is used in POST requests, e.g. signup when the form is not valid
#     post = TemplateView.get
#
# @secure_required
# @permission_required_or_403('change_profile', (get_profile_model(), 'user__username', 'username'))
# def profile_edit(request, username, edit_profile_form=MyProfile,
#                  template_name='userena/profile_form.html', success_url=None,
#                  extra_context=None, **kwargs):
#
#
#     user = get_object_or_404(get_user_model(), username__iexact=username)
#
#     profile = get_user_profile(user=user)
#
#     user_initial = {'first_name': user.first_name,
#                     'last_name': user.last_name}
#
#     form = edit_profile_form(instance=profile, initial=user_initial)
#
#     if request.method == 'POST':
#         form = edit_profile_form(request.POST, request.FILES, instance=profile,
#                                  initial=user_initial)
#
#         if form.is_valid():
#             profile = form.save()
#
#             if userena_settings.USERENA_USE_MESSAGES:
#                 messages.success(request, _('Your profile has been updated.'),
#                                  fail_silently=True)
#
#             if success_url:
#                 # Send a signal that the profile has changed
#                 userena_signals.profile_change.send(sender=None,
#                                                     user=user)
#                 redirect_to = success_url
#             else: redirect_to = reverse('userena_profile_detail', kwargs={'username': username})
#             return redirect(redirect_to)
#
#     if not extra_context: extra_context = dict()
#     extra_context['form'] = form
#     extra_context['profile'] = profile
#     return ExtraContextTemplateView.as_view(template_name=template_name,)


