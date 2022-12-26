from django.contrib import admin
from django.urls import path, re_path, include

# from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from home import views as home_views




urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += (
    
    re_path(r'^$', home_views.index_view),

)

urlpatterns.append(re_path(r'^api/', include('media.urls')))






if settings.DEBUG:
    urlpatterns += (
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,
                {'document_root': settings.STATIC_ROOT}),
                    )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(re_path(r'^__debug__/', include(debug_toolbar.urls)))


