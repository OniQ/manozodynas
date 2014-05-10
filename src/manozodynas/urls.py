from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import index_view
from .views import WordCreate, WordDelete, WordList, WordTranslation, TranslationCreate

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^words$', WordList.as_view(), name='words'),
    url(r'^word$', WordCreate.as_view(), name='word'),
    url(r'^word/(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word_delete'),
    url(r'^word/(?P<pk>\d+)/view/$', WordTranslation.as_view(), name='word_view'),
    url(r'^word/(?P<word>\d+)/translate/$', TranslationCreate.as_view(), name='word_translate'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
