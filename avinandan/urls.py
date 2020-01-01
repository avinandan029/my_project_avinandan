from django.conf.urls import include, url
from django.contrib import admin
from avinandanApp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/', views.registration_view),
    url(r'^$',views.Login_View),
    url(r'^home/',views.home_view),
    url(r'^contact/',views.contact_view),
    url(r'^services/',views.services_view),
    url(r'^feedback/',views.feedback_view),
    url(r'^gallery/',views.gallery_view)

]
