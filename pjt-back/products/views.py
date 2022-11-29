from django.shortcuts import render
import requests
from .serializers import DepositSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def make_depositDB(request):
    KEY = "6e2592277619abca4da5a340bc99bd77"

    fin_grp_list = [
    '020000',    # 은행
    '030300',    # 저축은행
    ]
    
    deposit_product_url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"

    for fin_grp in fin_grp_list:
        max_page = '1'
        params = {
            "auth" : KEY,
            "topFinGrpNo" : fin_grp,
            "pageNo" : max_page
        }
        # fin_grp별 open api 데이터 받아오기
        response = requests.get(deposit_product_url, params=params).json()
        max_page = int(response['result']['max_page_no']) # 조회할 수 있는 페이지 수

        for page in range(max_page):
            params = {
            "auth" : KEY,
            "topFinGrpNo" : fin_grp,
            "pageNo" : page
            }
            
            response = requests.get(deposit_product_url, params=params).json()
            deposit_products = response['result']['baseList']
            for product in deposit_products:
                serializer = SavingDepositSerializer(data=product)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
    return Response({'RESULT': 'OPEN API RECEIVED SUCCESSFUL!'}, status=status.HTTP_200_OK)
        

'''
            savedeposit = SavingDeposit()

            savedeposit.dcls_month = product.get("dcls_month")
            savedeposit.fin_co_no = product.get("fin_co_no")
            savedeposit.fin_prdt_cd = product.get("fin_prdt_cd")
            savedeposit.kor_co_nm = product.get("kor_co_nm")
            savedeposit.fin_prdt_nm = product.get("fin_prdt_nm")
            savedeposit.join_way = product.get("join_way")
            savedeposit.mtrt_int = product.get("mtrt_int")
            # 만기시점 약정이율 : 일반정기예금 금리",
            savedeposit.spcl_cnd = product.get("spcl_cnd")
            savedeposit.join_deny = product.get("join_deny")
            savedeposit.join_member = product.get("join_member")
            savedeposit.etc_note = product.get("etc_note")
            savedeposit.max_limit = product.get("max_limit")
            savedeposit.dcls_strt_day = product.get("dcls_end_day")
            savedeposit.dcls_end_day = product.get("dcls_end_day")
            savedeposit.fin_co_subm_day = product.get("fin_co_subm_day")


'''