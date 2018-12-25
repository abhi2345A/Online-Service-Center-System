from django.urls import path
from .views import (home, about, faq,
                    ProductCreateView, RepairCreateView, ComplaintCreateView,
                    ProductDetailView, RepairDetailView, ComplaintDetailView,
                    ProductUpdateView, RepairUpdateView, ComplaintUpdateView,
                    ProductDeleteView, RepairDeleteView, ComplaintDeleteView,
                    ReportListView, bill_info
                    )

urlpatterns = [
        path('', home, name='home'),
        path('about/', about, name='about'),
        path('faq/', faq, name='faq'),
        path('product_register/', ProductCreateView.as_view(), name='product-register'),
        path('product_repair/', RepairCreateView.as_view(), name='product-repair'),
        path('product_complaint/', ComplaintCreateView.as_view(), name='product-complaint'),
        path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
        path('product_repair/<int:pk>/', RepairDetailView.as_view(), name='repair-detail'),
        path('product_complaint/<int:pk>/', ComplaintDetailView.as_view(), name='complaint-detail'),
        path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
        path('product_repair/<int:pk>/update', RepairUpdateView.as_view(), name='repair-update'),
        path('product_complaint/<int:pk>/update', ComplaintUpdateView.as_view(), name='complaint-update'),
        path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
        path('product_repair/<int:pk>/delete/', RepairDeleteView.as_view(), name='repair-delete'),
        path('product_complaint/<int:pk>/delete/', ComplaintDeleteView.as_view(), name='complaint-delete'),
        path('report_check/', ReportListView.as_view(), name='report-check'),
        path('bill_info/', bill_info, name='bill-info')
        # path('status_check/', StatusListView.as_view(), name='status-check'),
    ]
