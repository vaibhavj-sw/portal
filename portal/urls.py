"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from employee import views as emp_views
from billing import views as bill_views
from django.conf.urls.static import static

urlpatterns = [
    path('portal/admin/', admin.site.urls),
    path("portal/", emp_views.homepage, name="homepage"),
    path("portal/register", emp_views.register_request, name="register"),
    path("portal/login", emp_views.login_request, name="login"),
    path("portal/logout", emp_views.logout_request, name="logout"),
    path("portal/password_reset", emp_views.password_reset_request, name="password_reset"),
    path('portal/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('portal/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('portal/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),    
    path("portal/search/", emp_views.search_lead, name="search_results"),

    path("portal/billing", bill_views.dashboard, name="dashboard"),
    path("portal/clients", bill_views.clients, name="clients"),
    path('portal/invoices',bill_views.invoices, name='invoices'),

    #Create URL Paths
    path('portal/invoices/create',bill_views.createInvoice, name='create-invoice'),
    path('portal/invoices/create-build/<slug:slug>',bill_views.createBuildInvoice, name='create-build-invoice'),

    #Delete an invoice
    path('portal/invoices/delete/<slug:slug>',bill_views.deleteInvoice, name='delete-invoice'),

    #PDF and EMAIL Paths
    path('portal/invoices/view-pdf/<slug:slug>',bill_views.viewPDFInvoice, name='view-pdf-invoice'),
    path('portal/invoices/view-document/<slug:slug>',bill_views.viewDocumentInvoice, name='view-document-invoice'),
    path('portal/invoices/email-document/<slug:slug>',bill_views.emailDocumentInvoice, name='email-document-invoice'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)