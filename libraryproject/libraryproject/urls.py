import apps.bookmodule.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apps.bookmodule.views.index), 
]
