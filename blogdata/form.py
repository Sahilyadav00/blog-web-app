from django import forms

class Blog(forms.Form):
    # <input name='email' type='email'>
    choices = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('politics', 'Politics')
    ]

    title = forms.CharField(max_length=100)
    post = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=choices)
    file = forms.FileField()

