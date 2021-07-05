
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from task_app.views import LandingPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('task_app.urls', namespace='task_app')),
    path('employees/', include('employee_app.urls', namespace='employee_app')),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
