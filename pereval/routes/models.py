from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Routes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    fam = models.CharField(max_length=255, verbose_name='Фамилия')
    otc = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'

class Level(models.Model):
    LEVEL = [
        ('1b','1Б'),
        ('2a','2A'),
        ('2b','2Б'),
        ('3a','3A'),
        ('3b','3Б'),
        ('4a','4A'),
        ('4b','4Б'),
        ('5b','5Б'),
        ('6a','6A'),
        ('6b','6Б')
    ]
    winter = models.CharField(max_length=2, choices=LEVEL, verbose_name='Зима')
    spring = models.CharField(max_length=2, choices=LEVEL, verbose_name='Весна')
    summer = models.CharField(max_length=2, choices=LEVEL, verbose_name='Лето')
    autumn = models.CharField(max_length=2, choices=LEVEL, verbose_name='Осень')

    def __str__(self):
        return f'Уровень сложности в зимнее время - {self.winter}, в весеннее - {self.spring}, в летнее - {self.summer}, в осеннее - {self.autumn}'

class Coords(models.Model):
     latitude = models.FloatField(max_length=30, verbose_name='Широта')
     longitude = models.FloatField(max_length=30, verbose_name='Долгота')
     height = models.IntegerField(verbose_name='Высота')

     def __str__(self):
         return f'широта - {self.latitude}, долгота - {self.longitude}, высота - {self.height}'


