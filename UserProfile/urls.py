from django.conf.urls import url

from UserProfile.views import ProfileView, ProfileUpdateView

urlpatterns = [
    url(r'^$', ProfileView.as_view(), name='profile'),
    url(r'^update/$', ProfileUpdateView.as_view())
]
