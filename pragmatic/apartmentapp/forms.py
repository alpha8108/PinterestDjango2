from django import forms

class MyForm(forms.Form):
    SGG_NM_CHOICES = [('choice1', 'choice1'), ('choice2', 'Choice 2'), ('choice3', 'Choice 3')]
    BUILD_YEAR_CHOICES = [(str(year), str(year)) for year in range(1970, 2025)]
    HOUSE_GBN_NM_CHOICES = [('apt', '아파트'), ('apt_complex', '연립다세대'), ('officetel', '오피스텔')]

    SGG_NM = forms.ChoiceField(label='지역구', choices=SGG_NM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    RENT_AREA = forms.FloatField(label='임대면적', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '평수를 입력하세요'}))
    RENT_FEE = forms.FloatField(label='임대료(만원)', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '임대료를 입력하세요'}))
    BUILD_YEAR = forms.ChoiceField(label='건축년도', choices=BUILD_YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    HOUSE_GBN_NM = forms.ChoiceField(label='건물용도', choices=HOUSE_GBN_NM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    BEFORE_GRNTY_AMOUNT = forms.FloatField(label='종전보증금', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': '종전 임대료를 입력하세요'}))
    BEFORE_MT_RENT_CHRGE = forms.FloatField(label='종전임대료', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': '종전 임대료를 입력하세요'}))
