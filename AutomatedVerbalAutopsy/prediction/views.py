from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import pickle
import os
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn import metrics
import pandas as pd
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import PredictionForm
from io import BytesIO
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from questionnaire.models import Shuhuda,Marehemu,Sababu
from django.http import FileResponse
import io
from django.utils import timezone
from reportlab.lib.units import inch

# Define Constant



MODELFILE = settings.MODEL_DIR + '/naive_bayes.pkl'
VECFILE = settings.MODEL_DIR + '/count_vectorizer.pkl'


with open(MODELFILE, 'rb') as f:
    model = pickle.load(f)

with open(VECFILE, 'rb') as f:
    vectorizer = pickle.load(f)  

# @login_required
# def index(request):
#     if request.method == 'POST':
#         #Get user inputs
#         inputs = request.POST.get('inputs')

#         # Check if inputs is a string
#         if isinstance(inputs, str):
#             # Convert inputs as a list
#             inputs = [inputs]
#         # Load the ML model
#         with open(MODELFILE, 'rb') as f:
#             model = pickle.load(f)

#         # Generate prediction using the model and user inputs
#         prediction = model.predict(inputs)


#         # Pass the prediction to the template
#         context = {'prediction': prediction}
        
#         return render(request, 'prediction/index.html', context)
#     return render(request, 'prediction/index.html')

# def predict_result(request,message=None):
#     username = request.user.username
#     # Extract the disease labels from the ground truth data
#     inputs =Marehemu.objects.order_by('-id').values_list('maelezo', flat=True).first()

#     # row_count = all_maelezo.count()
#     other_field= Marehemu.objects.all().order_by('-id').first()
   
#     # Check if inputs is a string
#     if isinstance(inputs, str):
#         inputs = [inputs]
    
#     # Load the ML model
#     with open(MODELFILE, 'rb') as f:
#         model = pickle.load(f)
    
#     # Generate prediction using the model and user inputs
#     prediction = model.predict(inputs)
#     prediction = str(prediction[0]) 
#     inputs = str(inputs[0]) 
#     return render(request, 'prediction/success.html',{'all_maelezo': inputs,  'username':username, 'other_field':other_field, 'prediction':prediction })

@login_required
def delete_questionnaire(request):
    username = request.user.username
    marehemu_to_delete = Marehemu.objects.latest('id')
    sababu_to_delete = marehemu_to_delete.sababu

    if request.method == 'POST':
        sababu_to_delete.delete()
        marehemu_to_delete.delete()
        return redirect('questionnaire:submit_form')

    context = {
        'object_to_delete': marehemu_to_delete,
        'username': username
    }
    return render(request, 'prediction/success.html', context)


@login_required
def predict_disease(request):
    username = request.user.username
    inputs =Marehemu.objects.order_by('-id').values_list('maelezo', flat=True).first()

    # row_count = all_maelezo.count()
    other_field= Marehemu.objects.all().order_by('-id').first()
   
    # Check if inputs is a string
    if isinstance(inputs, str):
        inputs = [inputs]

    # Transform the user input using the vectorizer
    user_input_vector = vectorizer.transform(inputs)

    # Predict the disease for the user input
    prediction = model.predict(user_input_vector)[0]

    # Get the probability scores for each disease
    disease_scores = model.predict_proba(user_input_vector)[0]

    # Convert the scores to percentages
    scores_percentage = [round(score * 100, 2) for score in disease_scores]
    inputs = str(inputs[0]) 
    marehemu_instance = get_object_or_404(Marehemu, id=other_field.id)
    sababu, created = Sababu.objects.get_or_create(
        Marehemu=marehemu_instance,
        defaults={'sababu': prediction}
    )
    # Prepare the data to pass to the template

    context = {
        'prediction': prediction,
        'diseases_scores': zip(model.classes_, scores_percentage),
        'all_maelezo': inputs,
        'username':username,
        'other_field':other_field
        }

    return render(request, 'prediction/success.html', context, )


@login_required
def success(request, message=None):
    username = request.user.username 
    cod_with_sababu_data = Sababu.objects.all()
    context = {
        'cod_with_sababu_data': cod_with_sababu_data,
        'username':username
    }
    return render(request, 'questionnaire/report.html', context)



# def report(request):
    sababu_values = Sababu.objects.all().order_by('-id')
    marehemu_values = []
    shuhuda_values = []

    for sababu in sababu_values:
        marehemu = sababu.Marehemu  # Access the related Marehemu object
        marehemu_values.append(marehemu)
        shuhuda_values.append(marehemu.shuhuda.all())

    combined_data = {
        'sababu_values': sababu_values,
        'marehemu_values': marehemu_values,
        'shuhuda_values': shuhuda_values
    }

    return render (request, 'questionnaire/report.html', {'combined_data': combined_data})


@login_required
def report(request):
    sababu_values = Sababu.objects.all().order_by('-id')
    marehemu_values = []
    shuhuda_values = []

    for sababu in sababu_values:
        marehemu = sababu.Marehemu  # Access the related Marehemu object
        marehemu_values.append(marehemu)
        shuhuda_values.append(marehemu.shuhuda.all())

    search_query = request.GET.get('query')
    if search_query:
        marehemu_values = Marehemu.objects.filter(jina_kwanza__icontains=search_query)

    # Create a paginator object with the desired number of items per page
    paginator = Paginator(marehemu_values, 10)  # Show 10 items per page

    # Get the current page number from the request
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page_obj = paginator.get_page(page_number)

    combined_data = {
        'sababu_values': sababu_values,
        'marehemu_values': page_obj,  # Pass the current page's object
        'shuhuda_values': shuhuda_values
    }

    return render(request, 'questionnaire/report.html', {'combined_data': combined_data})



@login_required
def download_report(request, marehemu_id): 
    current_date = timezone.now().date()
    marehemu = get_object_or_404(Marehemu, id=marehemu_id)
    shuhuda= get_object_or_404(Shuhuda ,id=marehemu_id)

    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')

    # Set the filename for the PDF
    response['Content-Disposition'] = 'attachment; filename="death_certificate.pdf"'

    # Create a PDF canvas
    
    p = canvas.Canvas(response)
 
    # Set the PDF content
    p.setFont("Helvetica", 12)
    p.drawString(200, 800, "University Of Dar-es-Salaam")
    p.drawString(150, 780, "Collage of Information and Communication Technology")
    p.drawString(200, 760, "Cause of Death Manipulation")
    p.drawString(180, 740, "-------------------------------------------------")
    p.drawString(220, 700, "DEATH CERTIFICATE")
    p.drawString(30, 670, "This is to verify that the following information has been obtained from the verbal autopsy of the deceased ")
    p.drawString(20, 650, f"registered under caretaker,{shuhuda.first_name} {shuhuda.middle_name} {shuhuda.last_name} with corresponds deceased's information below.")
    p.drawString(20, 620, f"Full Name: {marehemu.jina_kwanza} {marehemu.jina_pili} {marehemu.jina_mwisho} ")
    p.drawString(250, 620, f"Place of Death: {shuhuda.place}, {shuhuda.region}")
    p.drawString(20, 600, f"Sex: {marehemu.jinsia}")
    p.drawString(250, 600, f"Date of Birth: {marehemu.kuzaliwa}")
    p.drawString(20, 580, f"Date of Death: {marehemu.kufa}")
    p.drawString(250, 580, f"Place of Death: {marehemu.mahali}")
    p.drawString(20, 560, f"Cause of Death: {marehemu.sababu.sababu}")
    p.drawString(20, 520, f"Date: {current_date}")
    
    # Save the PDF
    p.showPage()
    p.save()

    return response

