from django import forms
from core.models import Enfermedad, Enfermedadmaes, Enfermedadmara


class EnfermedadmaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedad

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}
#		widgets = {
#			'description': forms.TextInput(),
#		}
		
class EnfermedadmaesmaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadmaes

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}

class EnfermedadmaramaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadmara

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}