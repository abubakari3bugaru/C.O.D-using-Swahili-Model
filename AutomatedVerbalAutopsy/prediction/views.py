from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import pickle
from django.http import HttpResponseBadRequest
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn import metrics
import pandas as pd
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import PredictionForm
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from questionnaire.models import Shuhuda,Marehemu,Sababu
from django.http import FileResponse
import io
from reportlab.lib.units import inch

# Define Constant


MODELFILE = settings.MODEL_DIR + '/naive_bayes.pkl'
VECFILE = settings.MODEL_DIR + '/count_vectorizer.pkl'


with open(MODELFILE, 'rb') as f:
    model = pickle.load(f)

with open(VECFILE, 'rb') as f:
    vectorizer = pickle.load(f)  

def index(request):
    if request.method == 'POST':
        #Get user inputs
        inputs = request.POST.get('inputs')

        # Check if inputs is a string
        if isinstance(inputs, str):
            # Convert inputs as a list
            inputs = [inputs]
        # Load the ML model
        with open(MODELFILE, 'rb') as f:
            model = pickle.load(f)

        # Generate prediction using the model and user inputs
        prediction = model.predict(inputs)


        # Pass the prediction to the template
        context = {'prediction': prediction}
        
        return render(request, 'prediction/index.html', context)
    return render(request, 'prediction/index.html')

def predict_result(request,message=None):
    username = request.user.username
    # Extract the disease labels from the ground truth data
    inputs =Marehemu.objects.order_by('-id').values_list('maelezo', flat=True).first()

    # row_count = all_maelezo.count()
    other_field= Marehemu.objects.all().order_by('-id').first()
   
    # Check if inputs is a string
    if isinstance(inputs, str):
        inputs = [inputs]
    
    # Load the ML model
    with open(MODELFILE, 'rb') as f:
        model = pickle.load(f)
    
    # Generate prediction using the model and user inputs
    prediction = model.predict(inputs)
    prediction = str(prediction[0]) 
    inputs = str(inputs[0]) 
    return render(request, 'prediction/success.html',{'all_maelezo': inputs,  'username':username, 'other_field':other_field, 'prediction':prediction })

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



def success(request, message=None):
    username = request.user.username 
    cod_with_sababu_data = Sababu.objects.all()
    context = {
        'cod_with_sababu_data': cod_with_sababu_data,
        'username':username
    }
    return render(request, 'questionnaire/report.html', context)





# def generate_report(request):
#     # Get the causes of death data
#     causes_of_death = COD.objects.all()

#     # Create a PDF document
#     buffer = BytesIO()
#     pdf = canvas.Canvas(buffer)

#     # Set up the PDF document
#     pdf.setTitle("Causes of Death Report")
#     pdf.setFont("Helvetica", 12)

#     # Write the causes of death data in the PDF
#     y = 750  # Initial y-coordinate
#     for cause in causes_of_death:
#         pdf.drawString(50, y, cause.maelezo)
#         y -= 20

#     # Save the PDF document
#     pdf.showPage()
#     pdf.save()

#     # Get the PDF content from the buffer
#     buffer.seek(0)
#     pdf_content = buffer.getvalue()
#     buffer.close()

#     # Create an HTTP response with the PDF content as a file attachment
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="causes_of_death_report.pdf"'
#     response.write(pdf_content)

#     return response



def generate_report(request):
    # Get the causes of death data
    causes_of_death = Sababu.objects.all()

    # Create a PDF document
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    # Set up the PDF document
    pdf.setTitle("Causes of Death Report")
    pdf.setFont("Helvetica", 12)

    # Write the causes of death data in the PDF
    y = 750  # Initial y-coordinate
    for cause in causes_of_death:
        pdf.drawString(60, 5, cause.jina_kwanza)
        pdf.drawString(65, 5, cause.jina_pili)
        pdf.drawString(70, 5, cause.jina_mwisho)
        pdf.drawString(50, -20, cause.maelezo)
      

    # Save the PDF document
    pdf.showPage()
    pdf.save()

    # Get the PDF content from the buffer
    buffer.seek(0)
    pdf_content = buffer.getvalue()
    buffer.close()

    # Render a preview page before download
    context = {'pdf_content': pdf_content}
    return render(request, 'prediction/report.html', context)

