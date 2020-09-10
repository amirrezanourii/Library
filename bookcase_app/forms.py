from django import forms

class RenewBookForm(forms.Form):
    renew_date = forms.DateTimeField(help_text='Enter a date between now and next 5 weeks.')
    # this is for security purposes
    def cleaned_renew_date(self):
        data = self.cleaned_data['renew_date']

        if data < datetime.date.today():
            raise ValidationError('Invalid date!')

        if data > datetime.date.today() + datetime.timedelta(weeks=5):
            raise ValidationError('Invalid date! Enter a date for 5 weeks later.')
        return data