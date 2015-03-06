from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'name/(?P<name>.+)$', 'birthdays.views.name_view', name='name_view'),
    url(r'(?P<birthday>\d{2}\.\d{2}\.\d{4})$', 'birthdays.views.birthday_view', name="birthday_view")
)
