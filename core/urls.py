from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# SET ADMIN TITLE
admin.site.site_header = "Multidb Project"
admin.site.site_title = "Admin Multidb"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/user/', include('apps.accounts.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path( 'api/listings/', include('apps.listings.urls')),
]
