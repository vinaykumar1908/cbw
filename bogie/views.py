from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from bogie.models import Bogie, RailPoint, FabBogieRegister, BogieDispatchRegister, BogieReceiveRegister
# Create your views here.
import datetime


@login_required
def fabshop(request):
    object1 = FabBogieRegister.objects.all().order_by('-RepDate')
        
        
    context = {
            'object': object1,
    }
    print('successful')
    return render(request, 'bogie/fabrication.html', context)

@login_required
def recdispatch(request):
    object1 = Bogie.objects.all().order_by('id')    
    p = BogieReceiveRegister.objects.all().order_by("-RecDate")
    q = BogieDispatchRegister.objects.all().order_by("-DispDate")
    print(p)
    context = {
        'object': object1,
        'object1': p,
        'object2' : q,
    }
    print('successful')
    return render(request, 'bogie/recdispatch.html', context)


@login_required
def BogieAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = Bogie.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(BogieType__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.BogieType
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'bogie/fabrication.html')

@login_required
def SourceAutocomplete(request):
    if request.is_ajax():
        print("request.GET")
        print(request.GET)
        if 'term' in request.GET:
            #print(term)
            qs = RailPoint.objects.all()
            print("qs")
            print(qs)
            itemTerm = request.GET.get('term')
            print("itemTerm")
            print(itemTerm)
            res = qs.filter(PlaceName__icontains=itemTerm)
            print("res")
            print(res)
            Item = list()
            for product in res:
                place_json = {}
                place_json = product.PlaceName
                Item.append(place_json)
                print("*------JsonResponse Start-----*")
                print(Item)
                print("*------JsonResponse End-----*")
            return JsonResponse(Item, safe=False)

            return render(request, 'bogie/recdispatch.html')


@login_required
def addFabBogie(request):
    if request.POST.get('Bogie') and request.POST.get('Quantity') and request.POST.get('datepicker'):
        r = Bogie.objects.all().filter(BogieType=request.POST.get('Bogie')).first()
        t = request.POST.get('Quantity')
        y = request.POST.get('datepicker')
        newDef = FabBogieRegister(BogieType=r, Quantity=t, RepDate=y, author=request.user)
        newDef.save()
        r.Quantity = r.Quantity + int(request.POST.get('Quantity'))
        r.Date = datetime.datetime.now() 
        r.save()
        print(r.Quantity)
        print(newDef)
        message = messages.success(request, "Fabrication Shop Record  Added: {}  {} supplied on {} ".format(newDef.Quantity ,newDef.BogieType, newDef.RepDate))
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    
    p = FabBogieRegister.objects.all().order_by("-RepDate")
    print(p)
    context = {
        #'messages': message,
        'object': p,
    }
    return render(request, 'bogie/fabrication.html', context)



@login_required
def receiptBogie(request):
    if request.POST.get('Bogie') and request.POST.get('Quantity') and request.POST.get('datepicker') and request.POST.get('Source'):
        r = Bogie.objects.all().filter(BogieType=request.POST.get('Bogie')).first()
        c = RailPoint.objects.all().filter(PlaceName=request.POST.get('Source')).first()
        t = request.POST.get('Quantity')
        y = request.POST.get('datepicker')
        newDef = BogieReceiveRegister(BogieType=r, Quantity=t, PlaceName=c, RecDate=y, author=request.user)
        newDef.save()
        r.Quantity = r.Quantity + int(request.POST.get('Quantity'))
        r.Date = datetime.datetime.now() 
        r.save()
        print(r.Quantity)
        print(newDef)
        message = messages.success(request, "Receipt Record  Added: {}  {} supplied on {} ".format(newDef.Quantity ,newDef.BogieType, newDef.RecDate))
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    object1 = Bogie.objects.all().order_by('id')
    p = BogieReceiveRegister.objects.all().order_by("-RecDate")
    q = BogieDispatchRegister.objects.all().order_by("-DispDate")
    print(p)
    context = {
        'object': object1,
        'object1': p,
        'object2' : q,
    }
    return render(request, 'bogie/recdispatch.html', context)


@login_required
def dispatchBogie(request):
    if request.POST.get('Bogie2') and request.POST.get('Quantity') and request.POST.get('datepicker1') and request.POST.get('Source2'):
        r = Bogie.objects.all().filter(BogieType=request.POST.get('Bogie2')).first()
        c = RailPoint.objects.all().filter(PlaceName=request.POST.get('Source2')).first()
        t = request.POST.get('Quantity')
        y = request.POST.get('datepicker1')
        newDef = BogieDispatchRegister(BogieType=r, Quantity=t, DispDate=y, PlaceName=c, author=request.user)
        newDef.save()
        r.Quantity = r.Quantity - int(request.POST.get('Quantity'))
        r.Date = datetime.datetime.now() 
        r.save()
        print(r.Quantity)
        print(newDef)
        message = messages.success(request, "Dispatch Record  Added: {}  {} supplied on {} ".format(newDef.Quantity ,newDef.BogieType, newDef.DispDate))
    else:
        message = messages.warning(request, "Please Fill All Entries ")

    object1 = Bogie.objects.all().order_by('id')
    p = BogieReceiveRegister.objects.all().order_by("-RecDate")
    q = BogieDispatchRegister.objects.all().order_by("-DispDate")
    print(p)
    context = {
        'object': object1,
        'object1': p,
        'object2' : q,
    }
    return render(request, 'bogie/recdispatch.html', context)