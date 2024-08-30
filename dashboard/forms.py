from django import forms
from info.models import Information, Project, Education



class EditProfileForm(forms.ModelForm):
	
	class Meta:
		model = Information
		exclude = ('born_date', 'address', 'cv')

class CreateProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		exclude = ('Slug',)

class CreateEducationForm(forms.ModelForm):

	class Meta:
		model = Education
		fields = '__all__'