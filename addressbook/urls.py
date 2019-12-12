from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts import views as contacts_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import api

router = DefaultRouter()
router.register(r'snippets', api.PersonViewSet)

urlAPIpatterns = [
    path('person/', api.PersonList.as_view()),
    path('person/<int:pk>/', api.PersonDetail.as_view())
]

urlAPIpatterns = format_suffix_patterns(urlAPIpatterns)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contacts_views.ContactView.as_view(), name ='contact-view'),
    path('success/', contacts_views.ContactAddSuccess.as_view(), name='contact-add-success'),
    path('fail/', contacts_views.ContactAddFail.as_view(), name='contact-add-fail'),
    path('add/db/', contacts_views.ContactAddView.as_view(), name='contact-add-db'),
    path('add/', contacts_views.ContactAddForm.as_view(), name='contact-add-view'),
    path('viewset/', include(router.urls))
] + urlAPIpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
