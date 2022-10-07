from django.shortcuts import render
from .models import Buyplan, Plan

# Create your views here.
def plan(request):
    postpaid_plan = Plan.objects.all().order_by('data')
    return render(request,'plan.html',{'postpaid_plan':postpaid_plan})

def buy_plan(request):
    if request.method=='POST':
        amount = request.POST.get('amount')
        data = request.POST.get('data')
        sms = request.POST.get('sms')
        roaming = request.POST.get('roaming')
        subscription = request.POST.get('subscription')
        plan = Buyplan(amount = amount, data = data, sms = sms, roaming = roaming, subscription = subscription)
        plan.save()

    return render(request,'plan_buy.html')


