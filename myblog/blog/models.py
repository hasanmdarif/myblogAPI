from django.db import models
from datetime import datetime
from  django.template.defaultfilters import slugify
class Categories(models.TextChoices):
    TECHNOLOGY = 'technology'
    DEVELOPMET = 'development'
    SOFTWARE = 'software'
    ENGINEERING = 'engineering'
    CODING = 'coding'

class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=70)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.ENGINEERING)
    thumbnail = models.ImageField(upload_to='photos/%Y.%m,%d/')
    excerpt = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, null=True)


    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact = original_slug).count()
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        super(BlogPost,self).save(*args, **kwargs)

        def __str__(self):
            return self.title