from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        reports_dashboard,
        name='reports_dashboard'
    ),

    path(
        'export/pdf/',
        export_pdf_report,
        name='export_pdf_report'
    ),

    path(
        'export/excel/',
        export_excel_report,
        name='export_excel_report'
    ),
]