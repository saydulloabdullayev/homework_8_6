from django.contrib import admin
from django.urls import path, include



#JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



#Swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Add List API",
      default_version='v1',
      description="Apps and news",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="No Litsenziya"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/figma/', include('app_figma.urls')),
   path('api/v1/add/', include('app_add.urls')),

   #SWAGGER
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   #JWT
   path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
