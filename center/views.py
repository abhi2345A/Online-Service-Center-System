from django.shortcuts import render, redirect
from .models import Product, Repair, Complaint
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView,
                                  CreateView,
                                  DeleteView)
from django.views.generic.base import ContextMixin, TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import ContextMixin, TemplateView
from django import forms
from django.db.models import Sum, Max, Avg, Min


def home(request):
    context = {}
    return render(request, 'center/home.html', context)


def about(request):
    context = {}
    return render(request, 'center/about.html', context)


def faq(request):
    context = {}
    return render(request, 'center/faq.html', context)


def bill_info(request):

    obj = Product.objects.all()
    # print(obj)
    total_price = 0
    if obj:
        for i in obj:
            if i.customer == request.user:
                total_price += i.price

        current_customer = 'default'
        max_price_prod = 0
        max_price_prodname = 'default'
        for j in obj:
            # print(j.customer)
            if j.customer == request.user:
                if j.price > max_price_prod:
                    current_customer = j.customer
                    max_price_prod = j.price
                    max_price_prodname = j.brand

        min_price_prodname = 'default'
        min_price_prod = 0
        min_price_prod = 9999999
        for j in obj:
            if j.customer == request.user:
                if j.price < min_price_prod:
                    min_price_prod = j.price
                    min_price_prodname = j.brand

    prod_name = max_price_prodname
    prod_name_min = min_price_prodname

    repair_cost = float(total_price) *0.1 + float(total_price)
    vat = 0.1* float(total_price)

    context = {
        'product' : Product.objects.all(),
        'total_price' : Product.objects.aggregate(Sum('price')),
        'avg_price' : Product.objects.aggregate(Avg('price')),
        'max_price' : Product.objects.aggregate(Max('price')),
        'min_price' : Product.objects.aggregate(Min('price')),
        'repair_cost' : int(repair_cost),
        'VAT' : int(vat),
        'max_prod' : prod_name,
        'min_prod' : prod_name_min,
        'max_price_prod' : max_price_prod,
        'min_price_prod' : min_price_prod,
        'total_pricex' : total_price,
        'current_customer' : current_customer
    }

    return render(request, 'center/bill_info.html', context)


class BillInfo(LoginRequiredMixin):
    template_name = 'center/bill_info.html'

    def get_context_data(self, **kwargs):
        context = super(BillInfo, self).get_context_data(**kwargs)
        context['product'] = Product.objects.all()
        context['total_price'] = Product.objects.aggregate(Sum('price'))
        context['average_price'] = Product.objects.aggregate(Avg('price'))
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'center/product_register.html'
    fields = ['product_type', 'brand',
                'model_no', 'product_retailer', 'purchase_date', 'city', 'zip_code', 'price']
    widgets = {'purchase_date': forms.DateInput(attrs={'class': 'datepicker'}),
            }

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your product has been registered!')
        return super().form_valid(form)


class RepairCreateView(LoginRequiredMixin, CreateView):
    model = Repair
    template_name = 'center/product_repair.html'
    fields = ['product_type', 'brand','phone_number', 'option_field','description', 'address']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your product repair request has been registered!')
        return super().form_valid(form)


class ComplaintCreateView(LoginRequiredMixin, CreateView):
    model = Complaint
    template_name = 'center/product_complaint.html'
    fields = ['product_type', 'brand', 'choice_field' ,'complaint_description', 'purchase_date', 'phone_no', 'suggestions']
    widgets = {'purchase_date': forms.DateInput(attrs={'class': 'datepicker'})}

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your complaint has been registered!')
        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'center/product_detail.html'


class RepairDetailView(LoginRequiredMixin, DetailView):
    model = Repair
    template_name = 'center/repair_detail.html'


class ComplaintDetailView(LoginRequiredMixin ,DetailView):
    model = Complaint
    template_name = 'center/complaint_detail.html'
    ordering = ['-purchase_date']


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'center/product_register.html'
    fields = ['product_type', 'brand',
                'model_no', 'product_retailer', 'purchase_date', 'city', 'zip_code']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your product details have been updated!')
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.customer


class RepairUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Repair
    template_name = 'center/product_repair.html'
    fields = ['product_type', 'brand','phone_number', 'description', 'address']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your repair request has been updated!')
        return super().form_valid(form)

    def test_func(self):
        repair = self.get_object()
        return self.request.user == repair.customer


class ComplaintUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Complaint
    template_name = 'center/product_complaint.html'
    fields = ['product_type', 'brand', 'choice_field' ,'complaint_description', 'purchase_date', 'phone_no', 'suggestions']

    def form_valid(self, form):
        form.instance.customer = self.request.user
        messages.success(self.request, f'Your complaint details have been updated! Thanks for your suggestions')
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.customer


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/center/report_check/'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.customer


class RepairDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Repair
    success_url = '/center/report_check/'

    def test_func(self):
        repair = self.get_object()
        return self.request.user == repair.customer


class ComplaintDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Complaint
    success_url = '/center/report_check/'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.customer


class BaseContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context_data = super(BaseContextMixin, self).get_context_data(**kwargs)
        data1 = Product.objects.all()
        context_data["key1"] = data1
        data2 = Repair.objects.all()
        context_data["key2"] = data2
        data3 = Complaint.objects.all()
        context_data["key3"] = data3

        current_customer = 'default'
        for j in data1:
            if j.customer == self.request.user:
                current_customer = j.customer
        context_data['current_customer'] = current_customer

        current_customer2 = 'default'
        for j in data2:
            if j.customer == self.request.user:
                current_customer2 = j.customer
        context_data['current_customer2'] = current_customer2

        current_customer3 = 'default'
        for j in data3:
            if j.customer == self.request.user:
                current_customer3 = j.customer
        context_data['current_customer3'] = current_customer3

        return context_data


class ReportListView(BaseContextMixin, TemplateView, LoginRequiredMixin):
    template_name = 'center/report_check.html'

    def get_context_data(self, **kwargs):
        context_data = super(ReportListView, self).get_context_data(**kwargs)
        return context_data



