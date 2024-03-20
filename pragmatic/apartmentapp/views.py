from django.shortcuts import render, HttpResponse

# Create your views here.

from .forms import MyForm

seoul_districts = [
    '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
    '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
    '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
]

def my_form_view(request):
    # form = MyForm()
    # return render(request, 'apartmentapp/predict.html', {'form': form})
    # if request.method == 'POST':
    #     # 폼 제출 시 기본값을 출력할 것이므로, 이를 알리는 변수 설정
    #     show_default = True
    #     # 다른 처리 작업 수행 가능
    #     return render(request, 'apartment/predict.html', {'show_default': show_default})
    # else:
    #     # 폼이 제출되지 않았을 때
    # return render(request, 'apartment/predict.html', {'show_default': '보증금을 예측해드립니다'})

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

            result = f'{sgg_nm}, {rent_area}평 대, 임대료{rent_fee}, 건축년도{build_year}, 건물용도{house_gbn_nm} 종전 보증금 {before_grnty_amount} 종전임대료{before_mt_rent_chrge}를 고르셨습니다.'

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


