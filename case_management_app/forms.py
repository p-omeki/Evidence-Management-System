from django import forms
from .models import Case, Evidence, Complainant


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            "case_title",
            "case_description",
            "case_officer",
            "created_at",
            "case_status",
            "case_outcome",
            "case_verdict",
        ]
        widgets = {"case_description": forms.Textarea(attrs={"rows": 4})}


class ComplainantForm(forms.ModelForm):
    class Meta:
        model = Complainant
        fields = [
            "case",
            "complainant_name",
            "complainant_phone_number",
            "complainant_email",
            "complainant_statement",
        ]
        widgets = {"complainant_statement": forms.Textarea(attrs={"rows": 4})}


class EvidenceCreationForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = [
            "type",
            "description",
            # add collection fields
            "collected_by",
            "collected_on",
            "collection_details",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "collection_details": forms.Textarea(attrs={"rows": 4}),
        }


class EvidenceAnalysisForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = [
            "analysis_details",
        ]
        widgets = {
            "analysis_details": forms.Textarea(attrs={"rows": 4}),
        }


class EvidencePresentationForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = [
            "presented_on",
            "presented_by",
            "presentation_details",
        ]
        widgets = {
            "presented_on": forms.DateInput(attrs={"type": "date"}),
            "presentation_details": forms.Textarea(attrs={"rows": 4}),
        }


class EvidenceDisposedForm(forms.ModelForm):
    class Meta:
        model = Evidence
        fields = [
            "disposed_on",
            "disposed_by",
            "disposal_details",
        ]
        widgets = {
            "disposed_on": forms.DateInput(attrs={"type": "date"}),
            "disposal_details": forms.Textarea(attrs={"rows": 4}),
        }
