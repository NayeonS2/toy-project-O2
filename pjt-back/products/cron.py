import time
import requests
from .models import Deposit
from django.db.models import Q
from .serializers import DepositSerializer
from apscheduler.schedulers.background import BackgroundScheduler


def make_depositDB():
    print(f'******{time.strftime("%H:%M:%S")}******')
    
    KEY = "6e2592277619abca4da5a340bc99bd77"
    fin_grp_list = [
    '020000',    # 은행
    '030300',    # 저축은행
    ]
    deposit_product_url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    
    total_products = []
    # db에 저장하기
    for fin_grp in fin_grp_list:
        
        params = {
            "auth" : KEY,
            "topFinGrpNo" : fin_grp,
            "pageNo" : '1'
        }
        
        # fin_grp별 open api 데이터 받아오기
        response = requests.get(deposit_product_url, params=params).json()
        # max_page_no 구하기
        max_page = int(response['result']['max_page_no']) # 조회할 수 있는 페이지 수
        
        for page in range(1, max_page + 1):
            params = {
            "auth" : KEY,
            "topFinGrpNo" : fin_grp,
            "pageNo" : page
            }
            
            response = requests.get(deposit_product_url, params=params).json()
            deposit_products = response['result']['baseList']
            total_products += deposit_products
            # # open API를 저장 및 업데이트
            for product in deposit_products:
                # get은 없으면 에러 발생시키기 때문에 에러처리하지 않도록 설정
                # 중복필드를 이용해서 유일한 레코드 불러오기
                deposit_set = Deposit.objects.filter(
                    Q(fin_co_no = product['fin_co_no']) & Q(fin_prdt_cd = product['fin_prdt_cd'])
                    )
                if deposit_set: # 업데이트 
                    deposit = Deposit.objects.get(
                    Q(fin_co_no = product['fin_co_no']) & Q(fin_prdt_cd = product['fin_prdt_cd'])
                    )
                    serializer = DepositSerializer(deposit, data=product)
                    if serializer.is_valid():
                        serializer.save()
                else: # 그냥 생성
                    serializer = DepositSerializer(data=product)
                    if serializer.is_valid():
                        serializer.save()
    
    deposits_DB = Deposit.objects.all()
            
    for deposit in deposits_DB:
        for product in total_products:
            if deposit.fin_co_no == product['fin_co_no'] and deposit.fin_prdt_cd == product['fin_prdt_cd']:
                break
        else:
            deposit.delete()
                        
    print("depositDB saved")
    print("************************")        
    
def main():
    sched = BackgroundScheduler()
    # 30분마다 실행
    sched.add_job(make_depositDB, 'interval', seconds=10, id='deposit')
    sched.start()
    # classapscheduler.triggers.interval.IntervalTrigger(weeks=0, days=0, hours=0, minutes=0, seconds=0, start_date=None, end_date=None, timezone=None, jitter=None)¶
