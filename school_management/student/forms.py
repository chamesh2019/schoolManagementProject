from django import forms


class StudentInsertForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    index_number = forms.CharField(max_length=10)
    sex = forms.ChoiceField(
        choices=(
            ('M', 'Male'),
            ('F', 'Female')
        )
    )
    ncf_identifier = None
    date_of_birth = forms.DateField()
    image_id = 'default'

    
