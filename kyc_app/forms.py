from unittest.util import _MAX_LENGTH
from django import forms  
from kyc_app.models import customer  
class NameForm(forms.ModelForm):  
    class Meta:  
        model = customer  
        fields = "__all__"  