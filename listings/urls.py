from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', shema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('listings.urls')),
]