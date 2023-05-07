from django.db import models


class Header(models.Model):
    name = models.TextField()
    sub = models.TextField(null=True)
    side = models.CharField(max_length=10, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    class YesNo (models.TextChoices):
        yes = 'Yes'
        no = 'No'

    class Size(models.TextChoices):
        small = 'Small'
        large = 'Large'
        pint = 'Pint'
        quart = 'Quart'
        can = 'Can'
        bottle = '20 oz.'

    name = models.TextField()
    subtitle = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    quart_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    bottle_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    menu_number = models.CharField(max_length=6, null=True, blank=True)
    lunch_number = models.CharField(max_length=6, null=True, blank=True)
    dinner_number = models.CharField(max_length=6, null=True, blank=True)
    lunch = models.CharField(max_length=4, choices=YesNo.choices, default=YesNo.no)
    dinner = models.CharField(max_length=4, choices=YesNo.choices, default=YesNo.no)
    substitute = models.CharField(max_length=4, choices=YesNo.choices, default=YesNo.no, null=True, blank=True)
    size = models.CharField(max_length=10, choices=Size.choices, null=True, blank=True)
    header = models.ForeignKey(Header, on_delete=models.CASCADE)
    spicy = models.CharField(max_length=4, choices=YesNo.choices, null=True, blank=True)
    number = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    combo_lunch_number = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    image = models.ImageField(upload_to="dishes/", null=True, blank=True)
    dinner_image = models.ImageField(upload_to="dishes/dinner-special/", null=True, blank=True)
    lunch_image = models.ImageField(upload_to="dishes/lunch/", null=True, blank=True)


    def __str__(self):
        return self.name
    
    def image_tag(self):
        return u'<img class="menu-item-image" src="%s"/>' % self.image.url #Not bad code
    image_tag.allow_tags = True

    def dinner_image_tag(self):
        return u'<img class="menu-item-image" src="%s"/>' % self.dinner_image.url #Not bad code
    dinner_image_tag.allow_tags = True

    def lunch_image_tag(self):
        return u'<img class="menu-item-image" src="%s"/>' % self.lunch_image.url #Not bad code
    lunch_image_tag.allow_tags = True