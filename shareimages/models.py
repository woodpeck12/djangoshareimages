from django.db import models

# Create your models here.
from django.conf import settings

class ShareIamge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created_by',on_delete='CASCADE')

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    who_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='who_like_images',blank=True)

    def __str__(self):
        return self.title , self.description

    def save(self, *args, **kwargs):
        if not self.slug:
	        self.slug = slugify(self.title)
	        #super(Image, self).save(*args, **kwargs)
	        super().save(*args,**kwargs)