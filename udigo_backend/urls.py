from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from udigo_backend.swaggers import swagger_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("places/", include("places.urls")),
    path("reviews/", include("reviews.urls")),
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + swagger_urls
    )
