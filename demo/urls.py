
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/'), name="admin-site"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
