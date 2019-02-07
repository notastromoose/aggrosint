from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Operation, Tools, Intel


def HomePageView(request):
	template_name = 'aggrosint/home.html'
	return render(request, template_name)
	
def ReportPageView(request):
	template_name = 'aggrosint/report.html'
	opcount = 0
	if (request.GET['op']):
		opcount = int(request.GET['op'])			

	operations = Operation.objects.all()[opcount:opcount+1]
	intel = Intel.objects.all().filter(operation=operations[0].name)
	print(operations)
	context = {
		"report":intel,
		"op":operations[0]
	}

	return render(request, template_name, context)

def OperationsPageView(request):
	model = Operation.objects.all()
	context_object_name = 'all_operations_list'
	context = {
		"operations": model
	}
	template_name = 'aggrosint/operations.html'
	return render(request, template_name, context)


def AnalystPageView(request):
	ops = Operation.objects.all()
	context_object_name = 'IntelObj'
	template_name = 'aggrosint/dashboard.html'

	context = {
		"ops":ops
	}


	if (request.method == 'POST'):
		subject = request.POST['subject']
		title = request.POST['title']
		category = request.POST['category']
		url = request.POST['url']
		just = request.POST['justification']

		intel = Intel(operation=subject, title=title, category=category, url=url, reason=just)
		intel.save()



	return render(request, template_name, context)


