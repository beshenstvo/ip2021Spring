from django.urls import path

from .views import HomePageView, ServicesPageView, ContactsPageView, ServicesDisablePageView, request_page_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("services", ServicesPageView.as_view(), name="services"),
    path("contacts", ContactsPageView.as_view(), name="contacts"),
    path("requests", request_page_view, name="requests"),
    path("services_disable", ServicesDisablePageView.as_view(), name="services_disable")
]
