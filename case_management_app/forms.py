from django import forms
from .models import Case, Evidence, Reporter, Victim


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


class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = [
            "case",
            "victim_name",
            "victim_phone_number",
            "victim_email",
            "victim_statement",
        ]
        widgets = {"victim_statement": forms.Textarea(attrs={"rows": 4})}


class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = [
            "case",
            "reporter_name",
            "reporter_phone_number",
            "reporter_email",
            "reporter_statement",
            "relationship_to_victim",
        ]
        widgets = {
            "reporter_statement": forms.Textarea(attrs={"rows": 4}),
            "relationship_to_victim": forms.Textarea(attrs={"rows": 2}),
        }


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
