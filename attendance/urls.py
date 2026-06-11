from django.urls import path
from . import views

urlpatterns = [
    path('',                    views.index,            name='index'),
    path('verify-roll/',        views.verify_roll,      name='verify_roll'),
    path('verify-otp/',         views.verify_otp,       name='verify_otp'),
    path('mark-attendance/',    views.mark_attendance,  name='mark_attendance'),
    path('success/',            views.success,          name='success'),
    path('marked-absent/',      views.marked_absent,    name='marked_absent'),
    # Admin
    path('admin-login/',        views.admin_login,      name='admin_login'),
    path('admin-verify-otp/',   views.admin_verify_otp, name='admin_verify_otp'),
    path('admin-logout/',       views.admin_logout,     name='admin_logout'),
    path('admin-dashboard/',    views.admin_dashboard,  name='admin_dashboard'),
]
