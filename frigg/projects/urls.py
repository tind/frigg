from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^projects/approve/$', views.approve_projects, name='approve_projects_overview'),
    url(r'^projects/approve/(?P<project_id>\d+)/$', views.approve_projects, name='approve_project'),
    url(r'^(?P<owner>[^/]+)/(?P<name>[^/]+).svg$', views.build_badge, name='build_badge'),
    url(r'^(?P<owner>[^/]+)/(?P<name>[^/]+)/(?P<branch>[^/]+).svg$', views.build_badge,
        name='build_branch_badge'),
    url(r'^(?P<owner>[^/]+)/(?P<name>[^/]+)/coverage.svg$', views.coverage_badge,
        name='coverage_badge'),
    url(r'^(?P<owner>[^/]+)/(?P<name>[^/]+)/(?P<branch>[^/]+)/coverage.svg$', views.coverage_badge,
        name='coverage_branch_badge'),
]
