from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.api.views import (
    FollowerAPIView,
    FollowerAddAPIView,
    ProfileAPIView,
    ProfileDetailsAPIView,
    ProfileImageDetailsAPIView,
    UserAPIView,
    UserDetailsAPIView,
    UserLoginAPIView,
)

urlpatterns = {
    # token maker
    url(r'^get-token/', obtain_auth_token, name='token'),

    # basic user login, info urls
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^user/$', UserAPIView.as_view(), name="user"),
    url(r'^user/(?P<username>[\w.@+-]+)/$',
        UserDetailsAPIView.as_view(), name="user-details"),

    # user profile related urls
    url(r'^user/profile/$', ProfileAPIView.as_view(), name="profile"),
    url(r'^user/profile/(?P<pk>[\w.@+-]+)/$',
        ProfileDetailsAPIView.as_view(), name="profile-details"),
    url(r'^user/profile/(?P<pk>[\w.@+-]+)/followers/$',
        FollowerAPIView.as_view(), name="followers"),
    url(r'^user/profile/image/(?P<pk>\d+)/$',
        ProfileImageDetailsAPIView.as_view(), name='profile-image-details'),


    url(r'^follow/$', FollowerAddAPIView.as_view(), name='follow'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
