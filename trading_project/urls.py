from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import health_check
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # Djoser URLs for user management
    path('auth/', include('djoser.urls.jwt')),  # JWT URLs (login/logout)


    # Health check endpoint
    path('api/health-check/', health_check, name='health_check'),

]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import health_check


# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('auth/', include('djoser.urls')),  # Includes registration and other auth-related URLs
#     path('auth/', include('djoser.urls.jwt')),  # JWT paths from djoser

#     path('api/mgicandles/', include('mgicandles.urls')),
    
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

#     # Health check endpoint
#     path('api/health-check/', health_check, name='health_check'),
# ]

# # Serving media files during development
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
