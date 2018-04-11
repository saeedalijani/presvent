from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from Event.models import Session, Presentation


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['sessions'] = Session.objects.all().order_by('-id')[0:5]
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'UserProfile/profile.html'

    def get_context_data(self, **kwargs):
        context = dict()
        context['presentations'] = Presentation.objects.filter(user=self.request.user)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'UserProfile/profile_update.html'
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = '/accounts/profile/'

    def get_object(self, queryset=None):
        return self.request.user
