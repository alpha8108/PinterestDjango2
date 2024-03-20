from django import forms

seoul_districts = [
    '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
    '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
    '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
]

def sgg_nm():
    global seoul_districts
    SGG_NM_CHOICES = []
    for sgg in seoul_districts:
        SGG_NM_CHOICES.append((sgg, sgg)) 
    return SGG_NM_CHOICES


class MyForm(forms.Form):
    SGG_NM_CHOICES = sgg_nm()
    BUILD_YEAR_CHOICES = [(str(year), str(year)) for year in range(1970, 2025)]
    HOUSE_GBN_NM_CHOICES = [('apt', '아파트'), ('apt_complex', '연립다세대'), ('officetel', '오피스텔')]

    SGG_NM = forms.ChoiceField(label='지역구', choices=SGG_NM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    RENT_AREA = forms.FloatField(label='임대면적', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '평수를 입력하세요'}))
    RENT_FEE = forms.FloatField(label='임대료(만원)', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '임대료를 입력하세요'}))
    BUILD_YEAR = forms.ChoiceField(label='건축년도', choices=BUILD_YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    HOUSE_GBN_NM = forms.ChoiceField(label='건물용도', choices=HOUSE_GBN_NM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    BEFORE_GRNTY_AMOUNT = forms.FloatField(label='종전보증금', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': '종전 임대료를 입력하세요'}))
    BEFORE_MT_RENT_CHRGE = forms.FloatField(label='종전임대료', min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': '종전 임대료를 입력하세요'}))
