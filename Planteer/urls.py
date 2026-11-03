
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("i18n/", include("django.conf.urls.i18n")),

    # Main routes
    path("", include("core.urls")),
    path("plants/", include("plants.urls")),

    # Arabic routes with unique namespaces
    path(
        "ar/",
        include(("core.urls", "core"), namespace="core_ar")
    ),
    path(
        "ar/plants/",
        include(("plants.urls", "plants"), namespace="plants_ar")
    ),

    # Authentication
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
