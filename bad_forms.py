class SignupPoor(forms.Form):
    """Form fails to play its role in forcing program to save sensitive info as a hash which is best practice."""
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    bank_number = forms.CharField(widget=forms.PasswordInput) #not secure field could be enhanced to protect data. 

