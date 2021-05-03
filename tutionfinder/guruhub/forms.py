from django.forms import ModelForm
from .models import Tutor


class TutorCreate(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'