from django.db import models


class Laptop(models.Model):
    brand_name = models.CharField('brand_name', max_length=50)
    model = models.CharField('model', max_length=50)
    processor = models.CharField('processor', max_length=50)
    video_card = models.CharField('video_card', max_length=50)
    monitor = models.CharField('monitor', max_length=50)
    memory = models.CharField('memory', max_length=50)
    hard_drive = models.CharField('hard_drive', max_length=50)
    height = models.IntegerField('height')
    width = models.IntegerField('width')
    depth = models.IntegerField('depth')
    img_url = models.URLField('url', max_length=400, null=True, blank=True)
    price = models.FloatField('price', null=True, blank=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Laptops'
        verbose_name_plural = 'Laptop'


class PC_table(models.Model):
    brand_name = models.CharField('brand_name', max_length=50)
    model = models.CharField('model', max_length=50)
    processor = models.CharField('processor', max_length=50)
    video_card = models.CharField('video_card', max_length=50)
    memory = models.CharField('memory', max_length=50)
    hard_drive = models.CharField('hard_drive', max_length=50)
    height = models.IntegerField('height')
    width = models.IntegerField('width')
    depth = models.IntegerField('depth')
    img_url = models.URLField('url', max_length=400, null=True, blank=True)
    price = models.FloatField('price',  null=True, blank=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'PC-tables'
        verbose_name_plural = 'PC-table'


class Mobile(models.Model):
    brand_name = models.CharField('brand_name', max_length=50)
    model = models.CharField('model', max_length=50)
    display = models.CharField('display', max_length=100)
    camera = models.CharField('camera', max_length=150)
    processor = models.CharField('processor', max_length=50)
    video_card = models.CharField('video_card', max_length=50)
    memory = models.CharField('memory', max_length=50)
    hard_drive = models.CharField('hard_drive', max_length=50)
    height = models.IntegerField('height')
    width = models.IntegerField('width')
    depth = models.IntegerField('depth')
    img_url = models.URLField('url', max_length=400, null=True, blank=True)
    price = models.FloatField('price',  null=True, blank=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'Mobiles'
        verbose_name_plural = 'Mobile'
