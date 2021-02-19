
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    published_time = models.TimeField('Time published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added = models.DateTimeField(blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    kbyte_limit = 100
    if filesize > kbyte_limit * 1024:
        raise ValidationError("Max file size is %sKB" % str(kbyte_limit))

class Person(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='staticfiles', blank=True, null=True, validators=[validate_image])
    int = models.IntegerField(default=9999)
    float = models.FloatField(default=8888.88)
    bool = models.BooleanField(default=False)
    dec = models.DecimalField(max_digits=10, decimal_places=2, default=9999.99)
    time = models.TimeField(default=now)
    date = models.DateField(default=now)
    datetime = models.DateTimeField(default=now)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.name

class Persona(Person):
    class Meta:
        proxy = True
