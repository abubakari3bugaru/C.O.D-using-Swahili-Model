from django.http import HttpResponse

def index(request):
    return HttpResponse("This is so good base")

#from django.shortcuts import render
#from django.http import HttpResponse
#from django.views.generic import View
#from django.contrib import messages
#from django.contrib import auth
#from .models import Shuhuda, Mhanga,Uchunguzi
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
#from .forms import SubmitForm,mhangaForm,UchunguziForm,SubmitForm1
#
#
#
#@login_required
#def shuhuda(request, message=None):
#    username = request.user.username  # Get the authenticated user's username
#    if request.method == 'POST':
#        form = SubmitForm(request.POST)
#        if form.is_valid():
#            #Form data is valid, process it here
#            form_data = Shuhuda(
#                first_name=form.cleaned_data['firstName'],
#                middle_name=form.cleaned_data['middleName'],
#                last_name=form.cleaned_data['lastName'],
#                place=form.cleaned_data['place'],
#                region=form.cleaned_data['region'],
#                shahidi=form.cleaned_data['shahidi'],
#                simu=form.cleaned_data['simu'],
#                uhusiano=form.cleaned_data['uhusiano'],
#                uhusiano_kipindi_kifo=form.cleaned_data['uhusiano_kipindi_kifo'],
#            )
#            # Save the form data to the database
#            form_data.save()
#
#            return redirect("/Questionnaire/Questionnaire1/")
#
#            # return render(request, 'form1.html')  # Render a success page after form submission
#    else:
#        form = SubmitForm()
#    return render(request, 'form.html', {'username': username, 'message': message, 'form': form})
#
#def mhanga(request, message=None):
#    username = request.user.username  # Get the authenticated user's username
#    if request.method == 'POST':
#        form = SubmitForm1(request.POST)
#        if form.is_valid():
#            form_mhanga = Mhanga(
#                jina_kwanza=form.cleaned_data['jina_kwanza'],
#                jina_pili=form.cleaned_data['jina_pili'],
#                jina_mwisho=form.cleaned_data['jina_mwisho'],
#                jinsia=form.cleaned_data['jinsia'],
#                ndoa=form.cleaned_data['ndoa'],
#                kuzaliwa=form.cleaned_data['kuzaliwa'],
#                kufa=form.cleaned_data['kufa'],
#                mahali=form.cleaned_data['mahali'],
#                maelezo=form.cleaned_data['maelezo'],
#                sababu1=form.cleaned_data['sababu1'],
#                sababu2=form.cleaned_data['sababu2'],
#            )
#            form_mhanga.save()
#            return render(request, 'form2.html')
#    else:
#        form = SubmitForm1()
#    return render(request, 'form1.html', {'username': username, 'message': message,'form': form})
#
#def uchunguzi(request, message=None):
#    username = request.user.username  # Get the authenticated user's username
#    if request.method == 'POST':
#        form = UchunguziForm(request.POST)
#        if form.is_valid():
#            #Form data is valid, process it here
#            form_uchunguzi = Uchunguzi(
#                magonjwa=form.cleaned_data['magonjwa'],
#                mengineyo=form.cleaned_data['mengineyo'],
#            )
#            # Save the form data to the database
#            form_uchunguzi.save()
#
#            return render(request, 'success.html')  # Render a success page after form submission
#    else:
#        form = UchunguziForm()
#    return render(request, 'form2.html', {'username': username, 'message': message, 'form': form})
#
#
#
## def mhanga(request):
##     if request.method == 'POST':
##         # Process the form data
##         jina_kwanza = request.POST.get('jina_kwanza')
##         jina_pili = request.POST.get('jina_pili')
##         jina_mwisho = request.POST.get('jina_mwisho')
##         jinsia = request.POST.get('jinsia')
##         haliNdoa = request.POST.get('ndoa')
##         kuzaliwa = request.POST.get('kuzaliwa')
##         kufa=request.POST.get('kufa')
##         mahali=request.POST.get('mahali')
##         maelezo=request.POST.get('maelezo')
##         sababu1=request.POST.get('sababu1')
##         sababu2=request.POST.get('sababu2')
##         # ... retrieve other form fields in a similar manner
#
##         # Perform any necessary validations or data processing
#
##         # Redirect to a success page
##         return redirect('success')
#
##     return render(request, 'Questionnaire1.html')
#
#
#
#
#
#
## def mhanga(request, message=None):
##     username = request.user.username  # Get the authenticated user's username
##     if request.method == 'POST':
##         form = SubmitForm1(request.POST)
##         if form.is_valid():
##             form.save()  # Save the form data to the database
##             return render(request, 'form2.html')
##     else:
##         form = SubmitForm1()
##     return render(request, 'form1.html', {'username': username, 'message': message, 'form': form})
#
## def uchunguzi(request, message=None):
##     username = request.user.username  # Get the authenticated user's username
##     if request.method == 'POST':
##         form = UchunguziForm(request.POST)
##         if form.is_valid():
##             form.save()  # Save the form data to the database
##             return render(request, 'success.html')  # Render a success page after form submission
##     else:
##         form = UchunguziForm()
#
##     return render(request, 'form2.html', {'username': username, 'message': message,'form': form})
#
#
#
#def success(request):
#    return render(request, 'success.html')
#
##function ya kuingiza data to database kwa mhanga
#
#
#def dashboard(request,message=None):
#    all_shuhuda=Shuhuda.objects.all()
#    row_count = all_shuhuda.count()
#    username = request.user.username 
#    return render(request, 'dashboard.html',{'all':all_shuhuda,'row_count': row_count ,'username': username,})
#
#
#def dashboardMhanga(request,message=None):
#    all_Mhanga=Mhanga.objects.all()
#    row_count = all_Mhanga.count()
#    username = request.user.username 
#    return render(request, 'dashboard.html',{'all_Mhangas':all_Mhanga,'row_count': row_count })
#
#def dashboardUchunguzi(request,message=None):
#    all_Uchunguzi=Uchunguzi.objects.all()
#    row_count = all_Uchunguzi.count()
#    # username = request.user.username 
#    return render(request, 'dashboard.html',{'all_Uchunguzis':all_Uchunguzi,'row_count': row_count })
#
#
