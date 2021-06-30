from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CallbackForm
from .models import Order


class HomePageView(FormView):
    template_name = "pages/home.html"
    form_class = CallbackForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ServicesPageView(FormView):
    template_name = "pages/services.html"
    form_class = CallbackForm
    success_url = reverse_lazy("services")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ContactsPageView(FormView):
    template_name = "pages/contacts.html"
    form_class = CallbackForm
    success_url = reverse_lazy("contacts")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@login_required
def request_page_view(request):
    template_name = "pages/requests.html"

    orders = Order.objects.filter(client=request.user)
    return render(request, template_name, {"orders": orders})


class ServicesDisablePageView(FormView):
    template_name = "pages/services_disable.html"
    form_class = CallbackForm
    success_url = reverse_lazy("services_disable")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
