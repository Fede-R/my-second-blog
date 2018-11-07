from django import forms
from core.models import Enfermedad, Enfermedadmaes, Enfermedadmara, Enfermedadsoho, Enfermedadsota, Enfermedadsora, Enfermedadtriho, Enfermedadtripla


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

class EnfermedadsohomaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadsoho

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}

class EnfermedadsotamaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadsota

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}

class EnfermedadsoramaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadsora

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}


class EnfermedadtrihomaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadtriho

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}


class EnfermedadtriplamaizForm(forms.ModelForm):

	class Meta:
		model = Enfermedadtriho

		fields = [
			'description',

		]
		labels = {
			'description': '',
		}