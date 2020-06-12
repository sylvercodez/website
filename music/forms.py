from django import forms
from django.forms import ModelForm
from .models import *

def CreateAlbum(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

def CreateSong(ModelForm):
    class Meta:
        model = Song
        Fields = '__all__'
        exclude = ['album'] 