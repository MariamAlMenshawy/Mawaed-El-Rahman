from django import forms
from .models import IftarTable

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

# forms.py
class NewTableForm(forms.ModelForm):
    governorate = forms.ChoiceField(
        choices=GOVERNORATE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select','placeholder': 'المحافظة'})
    )

    class Meta:
        model = IftarTable
        fields = ('title','description','governorate','long','lat')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المائدة'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'تفاصيل إضافية...'}),
            'long': forms.HiddenInput(attrs={'id': 'id_long'}),
            'lat': forms.HiddenInput(attrs={'id': 'id_lat'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        lat = cleaned_data.get('lat')
        long = cleaned_data.get('long')
        if not lat or not long:
            raise forms.ValidationError("يرجى تحديد موقع المائدة على الخريطة.")
        return cleaned_data
        