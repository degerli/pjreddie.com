
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class File(models.Model):
    upload = models.FileField(upload_to="files")
    def __str__(self):
        return self.upload.url


"""
class Page( models.Model ):
    title = models.CharField( max_length=100 )
    description = models.TextField(null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)
    visible=models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def html(self):
        return markdown_to_html( self.body, self.images.all() )

    def __str__( self ):
        return self.title

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="image" )
    project = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True, related_name = "images")

    def __str__( self ):
        return self.name
"""
