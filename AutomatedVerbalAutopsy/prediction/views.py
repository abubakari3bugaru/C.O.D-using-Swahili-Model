from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from django.conf import settings
from questionnaire.models import COD,CODWithSababu
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
    inputs =COD.objects.order_by('-id').values_list('maelezo', flat=True).first()

    # row_count = all_maelezo.count()
    other_field= COD.objects.all().order_by('-id').first()
   
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
    object_to_delete = COD.objects.latest('id')
    if request.method == 'POST':
        object_to_delete.delete()
        return redirect('questionnaire:submit_form')
    return render(request, 'prediction/success.html', {'object_to_delete': object_to_delete ,'username': username})

def predict_disease(request):
    username = request.user.username
    inputs =COD.objects.order_by('-id').values_list('maelezo', flat=True).first()

    # row_count = all_maelezo.count()
    other_field= COD.objects.all().order_by('-id').first()
   
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
    # Prepare the data to pass to the template
    context = {
        'prediction': prediction,
        'diseases_scores': zip(model.classes_, scores_percentage),
        'all_maelezo': inputs,
        'username':username,
        'other_field':other_field
        }

    return render(request, 'prediction/success.html', context, )

  


            
def save_questionnaire(request, message=None):
    username = request.user.username 
    if request.method == 'POST':
        cod = COD.objects.latest('id')
        sababu = request.POST.get('sababu')
    
        codwithSababu = CODWithSababu(
              sababu=sababu,
            )
        codwithSababu.save()

        # Redirect to the success page
        return redirect('prediction:success')

    return render(request, 'prediction/success.html', {'username': username })

def success(request, message=None):
    username = request.user.username 
    cod_with_sababu_data = CODWithSababu.objects.all()
    context = {
        'cod_with_sababu_data': cod_with_sababu_data,
        'username':username
    }
    return render(request, 'prediction/success1.html', context)

# def save_prediction(request):
#     if request.method == 'POST':
#         form = PredictionForm(request.POST)
#         if form.is_valid():
#             sababu = form.cleaned_data['sababu']
#             codwithSababu = CODWithSababu(
#               sababu=sababu,
#             )
#             codwithSababu.save()

#             # Save the `sababu` data to your desired model or perform any other action
            
#             return redirect('prediction:success')  # Replace 'prediction:success' with the appropriate URL name
#     else:
#         form = PredictionForm()
    
#     return render(request, 'prediction/success.html', {'form': form})


def generate_report(request):
    # Get the causes of death data
    causes_of_death = COD.objects.all()

    # Create a PDF document
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    # Set up the PDF document
    pdf.setTitle("Causes of Death Report")
    pdf.setFont("Helvetica", 12)

    # Write the causes of death data in the PDF
    y = 750  # Initial y-coordinate
    for cause in causes_of_death:
        pdf.drawString(50, y, cause.maelezo)
        y -= 20

    # Save the PDF document
    pdf.showPage()
    pdf.save()

    # Get the PDF content from the buffer
    buffer.seek(0)
    pdf_content = buffer.getvalue()
    buffer.close()

    # Create an HTTP response with the PDF content as a file attachment
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="causes_of_death_report.pdf"'
    response.write(pdf_content)

    return response

