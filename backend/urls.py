from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls', namespace='core')),
    path('breed/', include('backend.breed.urls', namespace='breed')),
    path('specie/', include('backend.specie.urls', namespace='specie')),
    path('coat/', include('backend.coat.urls', namespace='coat')),
    path('animal/', include('backend.animal.urls', namespace='animal')),
    path('project/', include('backend.project.urls', namespace='project')),
    path('gsearch/', include('backend.gsearch.urls', namespace='gsearch')),
    path('users/', include('backend.users.urls', namespace='user')),
    path('accounts/', include('backend.accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)