from django import forms
from django.forms import ModelForm
from documents.models import Document
from reports.models import Report

class NewDocumentForm(ModelForm):
    CERT_TYPES = (
                    ('O', 'Other document'),
                    ('DBA', 'TSA produced DBA'),
                    ('WS', 'TSA produced Weld Stud'),
                )
    class Meta:
        model = Document
        fields = ['type', 'file']
    primary = forms.BooleanField(label='Primary Document?', required=False)
    internal = forms.ChoiceField(label='Document Type', choices=CERT_TYPES)
    
class AttachDocumentForm(forms.Form):
    lot_number = forms.ModelChoiceField(queryset=Report.objects.all())
    primary = forms.BooleanField(label='Primary Document?', required=False)
