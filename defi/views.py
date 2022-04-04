from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import DPC, TC, Rake
from django.contrib import messages
# Create your views here.



class DefiHome(LoginRequiredMixin, TemplateView):
    template_name = 'deficiencies/defhome.html'

@login_required
def DefiHome2(request):
    dpc = DPC.objects.all()
    tc = TC.objects.all()
    rake = Rake.objects.all()
    info = zip(rake, dpc, tc)
    print(info)
    context = {
            'info': info,    
        }
    print('successful')
    return render(request, 'deficiencies/defhome.html', context)

@login_required
def AddRake(request):
    rake = Rake.objects
    if request.method == 'POST':
        newrake = Rake(Name=request.POST.get('RakeName'),author=request.user)
        newrake.save()
        for key, value in request.POST.items():
            if value.startswith("DPC"):
                r = rake.get(Name=request.POST.get('RakeName'))
                newDPC = DPC(RakeName=r, DPCName=value)
                newDPC.save()
            elif value.startswith("TC"):
                r = rake.get(Name=request.POST.get('RakeName'))
                
                
                newTC = TC(RakeName=r, TCName=value)
                newTC.save()
            else :
                pass
        message = messages.success(request, "Rake Added ")    

        
        dpc = DPC.objects.all()
        tc = TC.objects.all()
        rake = Rake.objects.all()
        info = zip(rake, dpc, tc)
        print(info)
        context = {
                'info': info,
                'message' : message  
            }
        print('successful')
        return render(request, 'deficiencies/defhome.html', context)

    else:
        message = messages.warning(request, "Rake Not Added ")
        dpc = DPC.objects.all()
    tc = TC.objects.all()
    rake = Rake.objects.all()
    info = zip(rake, dpc, tc)
    context = {
            'info': info,   
            'message' : message, 
        }
    return render(request, 'deficiencies/defhome.html', context)
    
