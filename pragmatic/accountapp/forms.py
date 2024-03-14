from django.contrib.auth.forms import UserCreationForm 

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #여기까지만 쓰면 UserCreationForm 랑 똑같은 폼

        self.fields['username'].disabled = True