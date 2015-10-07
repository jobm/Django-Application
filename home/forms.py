from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        #fields = ["full_name", "email"]
        exclude = ["last_update"]
        model = Student
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 120:
            raise forms.ValidationError("You may be too old for this class")
        elif age < 10:
            raise forms.ValidationError("You may be too young for this class")
        return age
        #return lambda x: x <= 11 and x >= 121, age

class FeedbackForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message == 'Dirty':
            message == 'Clean'
        print(message)
        return message
