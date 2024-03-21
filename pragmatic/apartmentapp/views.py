from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import * 

from joblib import load
import pandas as pd

# Create your views here.

from .forms import MyForm

seoul_districts = [
    '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
    '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
    '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
]

def predict_rent_gtn_model(model_path, SGG_NM, RENT_AREA, RENT_FEE, BUILD_YEAR, HOUSE_GBN_NM, BEFORE_GRNTY_AMOUNT, BEFORE_MT_RENT_CHRGE):
    # 모델 불러오기
    pipeline = load(model_path)

    # 데이터프레임 생성
    df = pd.DataFrame([{
        'SGG_NM': SGG_NM, 
        'RENT_AREA': RENT_AREA,   
        'RENT_FEE': RENT_FEE,    
        'BUILD_YEAR': BUILD_YEAR,   
        'HOUSE_GBN_NM': HOUSE_GBN_NM,  
        'BEFORE_GRNTY_AMOUNT' : BEFORE_GRNTY_AMOUNT,  
        'BEFORE_MT_RENT_CHRGE' : BEFORE_MT_RENT_CHRGE  
    }])

    # 예측 값 생성
    df['평수'] = df['RENT_AREA'] * 0.3025
    prediction = pipeline.predict(df)

    return prediction[0]

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # 폼에서 입력된 데이터 가져오기
            sgg_nm = form.cleaned_data['SGG_NM']
            rent_area = form.cleaned_data['RENT_AREA']
            rent_fee = form.cleaned_data['RENT_FEE']
            build_year = form.cleaned_data['BUILD_YEAR']
            house_gbn_nm = form.cleaned_data['HOUSE_GBN_NM']
            before_grnty_amount = form.cleaned_data['BEFORE_GRNTY_AMOUNT']
            before_mt_rent_chrge = form.cleaned_data['BEFORE_MT_RENT_CHRGE']


            # 여기서 종속되는 결과값 계산
            # 예: 결과 = rent_area * rent_fee + build_year * before_grnty_amount

            model_path = 'models/RENT_GTN_MODEL.joblib'  # 모델 파일 경로 (이렇게 하는게 맞나...?)
            result = predict_rent_gtn_model(model_path, sgg_nm, rent_area, rent_fee, build_year, house_gbn_nm, before_grnty_amount, before_mt_rent_chrge)
            # 어떻게 불러와야할 지 모르겠음 ....이게 된거 맞나..? 


            # 계산된 결과를 템플릿에 전달하여 출력
            return render(request, 'apartmentapp/predict.html', {'form':form,'result': result})
    else:
        form = MyForm()

    return render(request, 'apartmentapp/predict.html', {'form': form})











# 이건 html로 일일히 구현했을 떄 다시 부활예정 
    # BUILD_YEAR = [str(year) for year in range(1970, 2025)]
    # SGG_NM = [str(sgg_nm) for sgg_nm in seoul_districts ]

    # if request.method == "POST":
    #     return render(request, 'apartmentapp/predict.html',   {'BUILD_YEAR': BUILD_YEAR,
    #                                                            'SGG_NM' : SGG_NM, 
    #                                                            '보증금예측': 'POST METHOD!'})
    # else:
    #     return render(request, 'apartmentapp/predict.html',   {'BUILD_YEAR': BUILD_YEAR,
    #                                                            'SGG_NM' : SGG_NM, 
    #                                                            '보증금예측': 'GET METHOD!'})


