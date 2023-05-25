from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.contrib import auth
from .models import COD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator





@login_required
def cod(request, message=None):
    username = request.user.username  # Get the authenticated user's username
    if request.method == 'POST':
        # form = SubmitForm1(request.POST)
        # if form.is_valid():
            form_COD = COD(
                first_name=request.POST['firstName'],   # correction: firstName
                middle_name=request.POST['middleName'],  # correction: middleName
                last_name=request.POST['lastName'],  # correction: lastName
                place=request.POST['place'],
                region=request.POST['region'],
                shahidi=request.POST['shahidi'],
                simu=request.POST['simu'],
                uhusiano=request.POST['uhusiano'],
                uhusiano_kipindi_kifo=request.POST['uhusiano_kipindi_kifo'],
                jina_kwanza=request.POST['jina_kwanza'],
                jina_pili=request.POST['jina_pili'],
                jina_mwisho=request.POST['jina_mwisho'],
                jinsia=request.POST['jinsia'],
                ndoa=request.POST['ndoa'],
                kuzaliwa=request.POST['kuzaliwa'],  # correction: kuzaliwa_year
                kufa=request.POST['kufa'],  # kufa_year
                mahali=request.POST['mahali'],
                maelezo=request.POST['maelezo']
            )
            form_COD.save()
            return redirect('prediction:predict')
    
    return render(request, 'questionnaire/form.html', {'username': username, 'message': message})

def maelezo(request, message=None):
    all_maelezo = COD.objects.all()
    paginator = Paginator(all_maelezo, 10)  # Display 10 items per pag
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    row_count = COD.objects.count()
    username = request.user.username 
    return render(request, 'questionnaire/dashboard.html', {'page_obj': page_obj, 'username': username, 'row_count': row_count})


def dashboard(request, message=None):
     username = request.user.username 
     return render(request, 'questionnaire/dashboard.html',{'username': username, 'message': message})

