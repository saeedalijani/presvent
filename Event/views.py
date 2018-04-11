from django.http import Http404
from django.utils.timezone import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Event.models import Session, Presentation, SessionComment, PresentationComment
from Event.forms import PresentationForm, SessionCommentForm, PresentationCommentForm


class SessionListView(ListView):
    model = Session
    template_name = 'Event/session_list.html'
    paginate_by = 12


class SessionDetailView(DetailView):
    model = Session

    def get_context_data(self, **kwargs):
        context = super(SessionDetailView, self).get_context_data(**kwargs)
        context['presentations'] = Presentation.objects.filter(session=self.object, is_verified=True).order_by(
            'start_time')
        context['comments'] = SessionComment.objects.filter(session=self.object)
        context['comment_form'] = SessionCommentForm
        return context


class PresentationCreateView(LoginRequiredMixin, CreateView):
    model = Presentation
    form_class = PresentationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['session'] = Session.objects.get(id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.session = self.get_context_data().get('session')
        return super(PresentationCreateView, self).form_valid(form)

    def get_success_url(self):
        return '/event/' + str(self.kwargs.get('pk'))


class PresentationDetailView(DetailView):
    model = Presentation

    def get_queryset(self):
        self.queryset = Presentation.objects.filter(is_verified=True)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(PresentationDetailView, self).get_context_data(**kwargs)
        context['comments'] = PresentationComment.objects.filter(presentation=self.object)
        context['comment_form'] = PresentationCommentForm
        return context


class PresentationUpdateView(LoginRequiredMixin, UpdateView):
    model = Presentation
    form_class = PresentationForm

    def get_object(self, queryset=None):
        obj = super(PresentationUpdateView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class SessionCommentCreateView(LoginRequiredMixin, CreateView):
    model = SessionComment
    form_class = SessionCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['session'] = Session.objects.get(id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.session = self.get_context_data().get('session')
        form.instance.creation_datetime = datetime.now()
        return super(SessionCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return '/event/' + str(self.kwargs.get('pk'))


class PresentationCommentCreateView(LoginRequiredMixin, CreateView):
    model = PresentationComment
    form_class = PresentationCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['presentation'] = Presentation.objects.get(id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.presentation = self.get_context_data().get('presentation')
        form.instance.creation_datetime = datetime.now()
        return super(PresentationCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return '/event/presentation/' + str(self.kwargs.get('pk'))
