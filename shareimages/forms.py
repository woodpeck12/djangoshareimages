from django import forms
from .models import ShareIamge
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ShareImageCreateForm(forms.Model):
	class Meta:
		model = ShareIamge
		fields = ('title','url','description')
		widgets = {
			'url': forms.HiddenInput,
		}

	def clean_url(self):
		url = self.cleaned_data['url']
		check_url_extension = url.rsplit('.',1)[1].lower()
		if check_url_extension not in ['jpg','jpeg']:
			raise forms.ValidationError('you are trying to load incorrect format of image. image must be joeg or jpg')
		return url

	def save(self,commit=True,*args, **kwarg):
		saved_img = super().save(commit=False)
		img_url = self.cleaned_data['url']
		img_name = '{}.{}'.format(slugify(saved_img),img_url.rsplit('.',1)[1].lower())


		response= request.urlopen(img_url)
		saved_img.image.save(img_name,ContentFile(response.read()),save=False)

		if commit:
			saved_img.save()
		return saved_img
