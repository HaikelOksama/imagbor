from django.db import models
from django.templatetags.static import static

# Create your models here.
#class Tag(models.Model):
    #name = models.CharField(max_length=100, null=True)

class Image(models.Model):
    title   =  models.CharField(max_length=25)
    tags    =  models.CharField(max_length=25, null=True)
    #list    =  models.ForeignKey(Tag, on_delete=models.CASCADE)
    subtags = models.CharField(max_length=50, null=True)
    urls    =  models.CharField(max_length=200)
    row     =  models.IntegerField()
    hidden  = models.BooleanField(default=False)
    caption = models.CharField(max_length=200, default="high qualitY")
    
    def nature_len():
        return Image.objects.filter(tags='nature').count()

    def tag_list(self):
        return self.subtags

    def img_url(self):
        return static("imabor/{}".format(self.urls))

    def img_alt(self):
        return self.caption

    def img_title(self):
        return self.title

    def img_tags(self):
        return self.tags

    def nature_show(self):
        return Image.objects.filter(tags='nature')  

    def absolute_img_url(self):
        return f"/images/{self.id}"

    def tags_url(self):
        return f"/images/{self.subtags}"

    def tag():
        y = Image.objects.values_list('subtags')
        x = ('hewan','tumbuhan','tanah','air','kuno','modern','pencakar_langit','eastern','planet','bintang','galaxy','spaceship','anime','disney','karikatur','unik')
        return x

