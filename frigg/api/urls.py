from django.conf.urls import include, url
from rest_framework import routers

from .views import BuildViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'builds', BuildViewSet)

urlpatterns = [
    url(
        r'^workers/report/$',
        'frigg.api.views.report_build',
        name='worker_api_report_build'
    ),
    url(
        r'^partials/build/(?P<owner>[^/]+)/(?P<name>[^/]+)/(?P<build_number>\d+)/$',
        'frigg.api.views.partial_build_page',
        name='api_partial_build_page'
    ),
    url(
        r'^',
        include(router.urls)
    ),

]
