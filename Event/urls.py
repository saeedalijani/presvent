from django.conf.urls import url
from django.urls import path

from Event.views import SessionListView, SessionDetailView, PresentationCreateView, PresentationDetailView, \
    PresentationUpdateView, SessionCommentCreateView, PresentationCommentCreateView

urlpatterns = [
    url(r'^$', SessionListView.as_view()),
    path('<int:pk>/', SessionDetailView.as_view(), name='article-detail'),
    path('<int:pk>/presentation/', PresentationCreateView.as_view(), name='presentation-create'),
    path('presentation/<int:pk>/', PresentationDetailView.as_view(), name='presentation-detail'),
    path('presentation/<int:pk>/update/', PresentationUpdateView.as_view(), name='presentation-update'),
    path('<int:pk>/comment/', SessionCommentCreateView.as_view(), name='session-comment-create'),
    path('presentation/<int:pk>/comment/', PresentationCommentCreateView.as_view(), name='presentation-comment-create'),
]
