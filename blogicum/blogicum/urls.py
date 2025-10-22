from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.views.generic.edit import CreateView
from users.forms import UserCreationForm
from django.conf.urls.static import static

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.internal_error'

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
    path('auth/', include('django.contrib.auth.urls')),
    path('pages/', include('pages.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)), )

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
