from django import forms


class ContactForm(forms.Form):
    pupil_lastname = forms.CharField(label='Familiya', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pupil_firstname = forms.CharField(label='Ism', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pupil_birthday = forms.CharField(label="Tug'ulgan kun", widget=forms.TextInput(attrs={'class': 'form-control'}))
    pupil_class = forms.CharField(label="Qaysi sinfga o’qishga kelmoqchi", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mother_lastname = forms.CharField(label='Familiya', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_firstname = forms.CharField(label='Ism', widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_birthday = forms.CharField(label="Tug'ulgan kun", widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_work = forms.CharField(label="Ish joyi", widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_phone = forms.CharField(label="Telefon", widget=forms.TextInput(
        attrs={'type': 'tel', 'class': 'form-control'}))
    mother_email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_lastname = forms.CharField(label='Familiya', widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_firstname = forms.CharField(label='Ism', widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_birthday = forms.CharField(label="Tug'ulgan kun", widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_work = forms.CharField(label="Ish joyi", widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_phone = forms.CharField(label="Telefon", widget=forms.TextInput(
        attrs={'type': 'tel', 'class': 'form-control'}))
    father_email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    condition = forms.CharField(label="Ma'lumotlarni ishlatishga ruxsatingiz",
                                widget=forms.TextInput(attrs={'class': 'largerCheckbox', 'type': 'checkbox'}))


class SendEmailForm(forms.Form):
    subject = forms.CharField(label='Mavzu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Mavzu'}))
    first_name = forms.CharField(label='Mavzu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}))
    email = forms.CharField(label='Mavzu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(label='Mavzu', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Telefon'}))
    message = forms.CharField(label='Mavzu', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Xabarni bu erga yozing...'}))
