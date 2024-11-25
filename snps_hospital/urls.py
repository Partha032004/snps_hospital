"""
URL configuration for snps_hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# spns_hospital/urls.py
from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),  # Links to all URLs in user_management
]
# snps_hospital/urls.py

from django.contrib import admin
from django.urls import include, path
from user_management import views  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),
    path('', views.index, name='home'),  # Set the root URL to display the homepage
]

from django.urls import path
from user_management import views

urlpatterns = [
    path('give_prescription.html', views.give_prescription, name='give_prescription'),
    path('view_prescriptions.html', views.view_prescriptions, name='view_prescriptions'),
]

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/',admin.site.urls),
    path('admin_add_remove_user.html', views.admin_add_remove_user, name='admin_add_remove_user'),
    path('admin_dashboard.html', views.admin_dashboard, name='admin_dashboard'),
    path('admin_logout.html', views.admin_logout, name='admin_logout'),
    path('admin_financial_report_response.html', views.admin_financial_report_response, name='admin_financial_report_response'),
    path('admin_login.html', views.admin_login, name='admin_login'),
    path('admin_request_financial_report.html', views.admin_request_financial_report, name='admin_request_financial_report'),
    path('admin_review_feedback.html', views.admin_review_feedback, name='admin_review_feedback'),
    path('billing_staff_dashboard.html', views.billing_staff_dashboard, name='billing_staff_dashboard'),
    path('billing_staff_logout.html', views.billing_staff_logout, name='billing_staff_logout'),
    path('billing_staff_login.html', views.billing_staff_login, name='billing_staff_login'),
    path('cancel_appointments.html', views.cancel_appointments, name='cancel_appointments'),
    path('doctor_availability.html', views.doctor_availability, name='doctor_availability'),
    path('check_doctor_availability.html', views.check_doctor_availability, name='check_doctor_availability'),
    path('doctor_dashboard.html', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor_login.html', views.doctor_login, name='doctor_login'),
     path('doctor_logout.html', views.doctor_logout, name='doctor_logout'),
    path('forgot_password.html', views.forgot_password, name='forgot_password'),
    path('fpass_billStaff.html', views.fpass_billStaff, name='fpass_billStaff'),
    path('fpas_admin.html', views.fpas_admin, name='fpas_admin'),
    path('fpas_doctor.html', views.fpas_doctor, name='fpas_doctor'),
    path('fpas_regcler.html', views.fpas_regcler, name='fpas_regcler'),
    path('generate_bill.html', views.generate_bill, name='generate_bill'),
    #  path('give_prescription.html', views.give_prescription, name='give_prescription'),
    path('', views.index, name='index'),  # Homepage view
    path('list_doctors.html', views.list_doctors, name='list_doctors'),
    path('logout.html', views.logout_view, name='logout'),
    path('make_appointment.html', views.make_appointment, name='make_appointment'),
    path('medical_records.html', views.medical_records, name='medical_records'),
    path('patient_dashboard.html', views.patient_dashboard, name='patient_dashboard'),
    path('patient_login.html', views.patient_login, name='patient_login'),
    path('patient_sign_up.html', views.patient_sign_up, name='patient_sign_up'),
    path('process_payment.html', views.process_payment, name='process_payment'),
    path('register_patient.html', views.register_patient, name='register_patient'),
    path('registration_clerk_dashboard.html', views.registration_clerk_dashboard, name='registration_clerk_dashboard'),
    path('registration_clerk_logout.html', views.registration_clerk_logout, name='registration_clerk_logout'),
    path('registration_clerk_login.html', views.registration_clerk_login, name='registration_clerk_login'),
    path('request_financial_report.html', views.request_financial_report, name='request_financial_report'),
    path('request_invoice.html', views.request_invoice, name='request_invoice'),
    path('request_medical_history.html', views.request_medical_history, name='request_medical_history'),
    path('roles.html', views.roles, name='roles'),
    path('sign_up.html', views.sign_up, name='sign_up'),
    path('submit_feedback.html', views.submit_feedback, name='submit_feedback'),
    path('update_patient_info.html', views.update_patient_info, name='update_patient_info'),
    path('update_patient_status.html', views.update_patient_status, name='update_patient_status'),
    path('verify_otp.html', views.verify_otp, name='verify_otp'),
    path('view_appointments.html', views.view_appointments, name='view_appointments'),
    path('view_prescriptions.html', views.view_prescriptions, name='view_prescriptions'),
    path('prescribe.html', views.prescribe, name='prescribe.html')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)