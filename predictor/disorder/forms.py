from django import forms

class SymptomForm(forms.Form):
    features = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']  # Replace with your actual column names
    feature1 = forms.CharField(label='Feature 1')
    feature2 = forms.CharField(label='Feature 2')
    feature3 = forms.IntegerField(label='Feature 3')
    feature4 = forms.CharField(label='Feature 4')
    feature5 = forms.CharField(label='Feature 5')
