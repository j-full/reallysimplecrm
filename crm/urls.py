from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path("contact/new/", views.contact_new, name="contact_new"),
    path('contact/<int:pk>/edit/', views.ContactEdit.as_view(), name='contact_edit'),
    path('contact/<int:pk>/delete/', views.ContactDelete.as_view(), name='contact_delete'),
    path("contact/<int:pk>/", views.ContactDetail.as_view(), name="contact_detail"),
    path("contact/<int:pk>/send-postcard", views.send_postcard, name="send_postcard"),
    path('export-xls', views.export_xls, name='export_xls'),
    path('import-xls', views.import_xls, name='import_xls'),
]