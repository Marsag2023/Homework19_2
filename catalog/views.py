from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy


from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Version


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        # context = self.get_context_data()
        # formset = context['formset']
        # if formset.is_valid():
        #     self.object = form.save()
        #     formset.instance = self.object
        #     formset.save()
        #     return super(ProductCreateView, self).form_valid(form)
        # else:
        #     return self.form_invalid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset(*args, **kwargs)
        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(version_now=True)
            if active_versions:
                product.active_version = active_versions.last().version_name
            else:
                product.active_version = 'Нет активной версии'
        context_data['object_list'] = products
        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        active_version = versions.filter(version_now=True).last()
        if active_version:
            product.active_version = active_version.version_name
        else:
            product.active_version = 'Нет активной версии'
        context_data['object'] = product
        context_data['version'] = product.active_version
        return context_data


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super(ProductUpdateView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('first_name', 'last_name', 'phone', 'message', 'email')
    template_name = 'catalog/contacts_form.html'
    success_url = reverse_lazy('catalog:contacts_list')
