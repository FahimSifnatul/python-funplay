from django import forms
from .models import ImageToText

class ImageToTextForm(forms.ModelForm):
	class Meta:
		model  	= ImageToText
		fields 	= '__all__'
		widgets = {
			'image_to_text' : forms.ClearableFileInput(\
								attrs={'id':'image_to_text_image'}),
		}

class RootsOfPolynomialEqForm(forms.Form):
	roots_of_polynomial_eq = forms.CharField(widget=forms.TextInput(\
								attrs={
									'class':'form-control',\
									'placeholder':'enter x**2-4 of eq x**2-4=0',
								}))

class TextToWordcloud(forms.Form):
	text_to_wordcloud = forms.CharField(widget=forms.Textarea(\
								attrs={
									'class':'form-control',
									'placeholder':'Enter you text to convert to WordCloud',
								}))