from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GOVERNORATE_CHOICES = [
    ('Cairo', 'القاهرة'),
    ('Giza', 'الجيزة'),
    ('Dakahlia', 'الدقهلية'),
    ('Damietta','دمياط'),
    ('Alexandria', 'الإسكندرية'),
    ('Sharkia', 'الشرقية'),
    ('Qalyubia', 'القليوبية'),
    ('Beheira', 'البحيرة'),
    ('Menofia', 'المنوفية'),
    ('Fayoum', 'الفيوم'),
    ('Minya', 'المنيا'),
    ('Asyut', 'أسيوط'),
    ('Sohag', 'سوهاج'),
    ('Beni Suef', 'بني سويف'),
    ('Red Sea', 'البحر الأحمر'),
    ('New Valley', 'الوادي الجديد'),
    ('Luxor', 'الأقصر'),
    ('Qena', 'قنا'),
    ('Aswan', 'أسوان'),
    ('Ismailia', 'الإسماعيلية'),
    ('Suez', 'السويس'),
    ('North Sinai', 'شمال سيناء'),
    ('South Sinai', 'جنوب سيناء'),
]

class IftarTable(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    governorate = models.CharField(max_length=20,choices=GOVERNORATE_CHOICES)

