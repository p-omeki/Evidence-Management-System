from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Case, Evidence, Complainant
from .forms import (
    CaseForm,
    ComplainantForm,    
    EvidenceCreationForm,
    EvidenceAnalysisForm,
    EvidencePresentationForm,
    EvidenceDisposedForm,
)
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from user_app.decorators import itofficer_required


@login_required
def register_case(request):
    if request.method != "POST":
        case_form = CaseForm()
        complainant_form = ComplainantForm()       
    else:
        case_form = CaseForm(request.POST)
        complainant_form = ComplainantForm(request.POST)
      
        if case_form.is_valid() and complainant_form.is_valid():   
            case = case_form.save(commit=False)
            complainant = complainant_form.save(commit=False)          
            case.case_officer = request.user
            case.save()

            complainant.case = case          
            complainant.save()
            
            messages.success(request, "Case registered successfully!")
            return redirect("case_management_app:registered_cases")
        else:
            messages.error(
                request, f"There was an error durig form submission. Please try again."
            )

    context = {
        "case_form": case_form,
        "complainant_form": complainant_form,       
        "section": "register_case",
    }
    template_name = "register_case.html"
    return render(request, template_name, context)


def registered_cases(request):
    cases = Case.objects.all()

    context = {"cases": cases, "section": "registered_cases"}
    template_name = "registered_cases.html"
    return render(request, template_name, context)


def registered_case(request, serial_number):
    case = get_object_or_404(Case, serial_number=serial_number)
    evidences = Evidence.objects.filter(case=case)
    complainants = Complainant.objects.filter(case=case)
  
    context = {
        "case": case,
        "evidences": evidences,
        "complainants": complainants,       
    }
    template_name = "registered_case.html"
    return render(request, template_name, context)


def create_evidence(request, serial_number):
    case = Case.objects.get(serial_number=serial_number)

    if request.method != "POST":
        evidence_form = EvidenceCreationForm()
    else:
        evidence_form = EvidenceCreationForm(request.POST, request.FILES)
        if evidence_form.is_valid():
            evidence = evidence_form.save(commit=False)
            evidence.case = case
            evidence.case_officer = case.case_officer
            evidence.save()

            messages.success(request, "Evidence added successfully!")
            return redirect(
                "case_management_app:registered_case", serial_number=serial_number
            )
        else:
            errors = list()

            for field, error in evidence_form.errors.items():
                errors.append(f"{field}: {error}")

            messages.error(request, f"{errors}")

    context = {
        "evidence_form": evidence_form,
        "case": case,
        "section": "create_evidence",
    }
    template_name = "create_evidence.html"
    return render(request, template_name, context)


def analyse_evidence(request, evidence_id):
    evidence = Evidence.objects.get(id=evidence_id)

    if request.method != "POST":
        evidence_form = EvidenceAnalysisForm(instance=evidence)
    else:

        evidence_form = EvidenceAnalysisForm(
            request.POST, request.FILES, instance=evidence
        )
        if evidence_form.is_valid():
            evidence = evidence_form.save(commit=False)
            evidence.is_analysed = True
            evidence.analysed_by = request.user
            evidence.analysed_on = timezone.now()
            evidence.save()

            messages.success(request, "Evidence analysed successfully!")
            return redirect(
                "case_management_app:registered_case",
                serial_number=evidence.case.serial_number,
            )
        else:
            errors = list()

            for field, error in evidence_form.errors.items():
                errors.append(f"{field}: {error}")

            messages.error(request, f"{errors}")

    context = {
        "evidence": evidence,
        "evidence_form": evidence_form,
        "section": "analyse_evidence",
    }
    template_name = "analyse_evidence.html"
    return render(request, template_name, context)


def presented_evidence(request, evidence_id):
    evidence = Evidence.objects.get(id=evidence_id)

    if request.method != "POST":
        evidence_form = EvidencePresentationForm(instance=evidence)
    else:
        evidence_form = EvidencePresentationForm(
            request.POST, request.FILES, instance=evidence
        )
        if evidence_form.is_valid():
            evidence = evidence_form.save(commit=False)
            evidence.is_presented = True
            evidence.presented_by = request.user
            evidence.presented_on = timezone.now()
            evidence.save()

            messages.success(request, "Evidence was presented successfully!")
            return redirect(
                "case_management_app:registered_case",
                serial_number=evidence.case.serial_number,
            )
        else:
            errors = [
                f"{field}: {error}" for field, error in evidence_form.errors.items()
            ]
            messages.error(request, f"{errors}")

    context = {
        "evidence": evidence,
        "evidence_form": evidence_form,
        "section": "presented_evidence",
    }
    template_name = "presented_evidence.html"
    return render(request, template_name, context)

@itofficer_required
def disposed_evidence(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)

    if request.method == "POST":
        form = EvidenceDisposedForm(request.POST, instance=evidence)
        if form.is_valid():
            updated_evidence = form.save(commit=False)
            updated_evidence.is_disposed = True
            updated_evidence.disposed_by = request.user
            updated_evidence.save()

            messages.success(request, "Evidence disposed successfully!")
            return redirect(
                "case_management_app:registered_case",
                serial_number=evidence.case.serial_number,
            )
        else:
            messages.error(
                request, "There was an error during form submission. Please try again."
            )
    else:
        form = EvidenceDisposedForm(instance=evidence)

    context = {
        "form": form,
        "section": "disposed_evidence",
    }
    template_name = "disposed_evidence.html"
    return render(request, template_name, context)


@itofficer_required
def restore_evidence(request, evidence_id):
    evidence = get_object_or_404(Evidence, id=evidence_id)

    if request.user.is_itofficer:
        evidence.is_disposed = False
        evidence.save()

        messages.success(request, "Evidence restored successfully!")
        return redirect(
            "case_management_app:registered_case", evidence.case.serial_number
        )
    else:
        messages.error(request, "You do not have permission to restore evidence.")
        return redirect(
            "case_management_app:registered_case", evidence.case.serial_number
        )

# Restore Case
def restore_case(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    if request.user.is_itofficer:
        case.disposed = False
        case.save()
        messages.success(request, "Case restored successfully!")
        return redirect("case_management_app:registered_case", case.serial_number)
    else:
        messages.error(request, "You do not have permission to restore cases.")
        return redirect("case_management_app:registered_cases")
