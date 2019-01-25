from django.shortcuts import render
from django.db.models import Avg, Count, Min, Sum
from expenses.models import Expense
# Create your views here.
def reports(request):
	object_list=[]
	exp_sum=0
	if request.method=="POST":
		object_list=Expense.objects.filter(datetime__month=request.POST.get("month"))
		exp_sum = object_list.aggregate(Sum('amount')).get("amount__sum")
	return render(request,"expenses/reports.html",
		{"object_list":object_list,"exp_sum":exp_sum}
		)
