from django.shortcuts import render
from django_daraja.mpesa import utils
from django.http import HttpResponse,JsonResponse
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime
from django.views import View

cl=MpesaClient()
stk_push_callback_url='https://api.darajambili.com/express-payment'
b2c_callback_url='http;//api.darajambili.com/b2c/result'

def oauth_success(request):
    r=cl.auth_token()
    return JsonResponse(r,safe=False)

def index(request):
    if request.method=="POST":
        phone_number=request.POST.get('phone')
        amount=request.POST.get('amount')
        amount=int(amount)
        account_reference='MZIZA NILIPE'
        transaction_reference='Stk push ref'
        callback_url=stk_push_callback_url
        r=cl.stk_push(phone_number,amount,account_reference,transaction_reference,callback_url)
        return JsonResponse(r.response_description,safe=False)

    return render(request,'index.html')




