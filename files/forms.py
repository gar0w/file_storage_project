# files/forms.py
from django import forms
from .models import Image, Video, Document

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'document_file']
