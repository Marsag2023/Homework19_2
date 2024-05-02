from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from catalog.models import Product, Contacts


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('first_name', 'last_name', 'phone', 'message', 'email')
    template_name = 'catalog/contacts_form.html'
    success_url = reverse_lazy('catalog:contacts_list')
