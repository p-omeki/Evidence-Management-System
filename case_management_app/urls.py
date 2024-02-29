from django.urls import path
from . import views


app_name = "case_management_app"

urlpatterns = [
    path("case/create/", views.register_case, name="register_case"),
    path("case/list/", views.registered_cases, name="registered_cases"),
    path(
        "case/<int:serial_number>/", views.registered_case, name="registered_case"
    ),
    path("evidence/create/<int:serial_number>/", views.create_evidence, name="create_evidence"),
    path("evidence/analyse/<int:evidence_id>/", views.analyse_evidence, name="analyse_evidence"),
    path("evidence/presented/<int:evidence_id>/", views.presented_evidence, name="presented_evidence"),
    path("evidence/disposed/<int:evidence_id>/", views.disposed_evidence, name="disposed_evidence"),
    path('case/<int:case_id>/restore/', views.restore_case, name='restore_case'),
    path("evidence/restore/<int:evidence_id>/", views.restore_evidence, name="restore_evidence"),
    
]


