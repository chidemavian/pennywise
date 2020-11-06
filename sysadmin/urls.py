
from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, TemplateView


urlpatterns = patterns('sysadmin.views',
    # Examples:
    #*****INCOME****************
    url(r'^income/$', 'setincome'),
    url(r'^myincome/$', 'myincome'),
    url(r'^income/edit/$', 'editmyincome'),
    url(r'^income/change/(\d+)/$', 'change'),
    url(r'^income/remove/(\d+)/$', 'deletedate'),


    #******BUDGET*****************
    url(r'^budget/$', 'budget'),
    url(r'^mybudget/$', 'mybudget'),
    url(r'^budget/edit/$', 'editmybudget'),
    url(r'^budget/change/(\d+)/$', 'bugchange'),
    url(r'^budget/remove/(\d+)/$', 'deletebug'),


    #******EVENTS****************
    url(r'^event/$', 'setevent'),
    url(r'^myevent/$', 'myevent'),
    url(r'^myevent/edit/$', 'editmyevent'),
    url(r'^event/revent/$','revent'),
    url(r'^myevent/add/(\d+)/$', 'addevent'),
    url(r'^mmme/edit/$', 'deletebug'),

    url(r'^expenses/edit/$','expenses'),
    url(r'^expenses/change/(\d+)/$', 'editexpen'),
    url(r'^expenses/remove/(\d+)/$', 'delexpen'),
    
   
)
