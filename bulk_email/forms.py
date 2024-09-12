from django import forms
import csv
from django.http import HttpResponse

def handle_uploaded_file(f):
    reader = csv.reader(f)
    emails = [row[0] for row in reader]  # Assuming emails are in the first column
    return emails

class EmailUploadForm(forms.Form):
    csv_file = forms.FileField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    schedule_time = forms.DateTimeField(required=False)
