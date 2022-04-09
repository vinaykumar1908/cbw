from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
import datetime
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
# from .forms import registerStockRecievedForm, registerStockDispatchROHform, registerStockDispatchSicklineform, registerStockDispatchedYardform, registerStockDispatchedTrainDutyform
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from .forms import ModuleRecievedForm, ModuleDefectForm
from django.db.models import Q
#from sidingz.models import ModuleRecieved

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
def LetterView(request):
    
    return render(request, 'letters/confidentialframe.html')

def LetterPrintPdf(request):
    
    print("****************")
    To = request.POST.get('To')
    date = request.POST.get('datepicker1')
    Designation = request.POST.get('Designation')
    Address = request.POST.get('Address')
    subject = request.POST.get('subject')
    matter = request.POST.get('matter')
    cc1 = request.POST.get('cc1')
    cc2 = request.POST.get('cc2')
    cc3 = request.POST.get('cc3')
    cc4 = request.POST.get('cc4')
    print(cc4)
    if date == '':
        date = datetime. datetime. now(). date()
    template_path = 'letters/confidentialpdf.html'
    user = request.user
    context = {
        'date' : date,
        'To' : To,
        'Designation' : Designation,
        'Address' : Address,
        'subject' : subject,
        'matter' : matter,
        'cc1' : cc1,
        'cc2' : cc2,
        'cc3' : cc3,
        'cc4' : cc4,
        'user' : user,
    }
    print(date)
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response