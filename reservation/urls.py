from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf.urls.static import static
from reservation import settings


urlpatterns = [
    path('hotel_reservation/', include('hotel_reservation.urls')),
    path('admin/', admin.site.urls),
path('', RedirectView.as_view(url='hotel_reservation/'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



