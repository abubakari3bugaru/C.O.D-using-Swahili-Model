
from django.shortcuts import render, redirect
from django.conf import settings
from questionnaire.models import COD
from .models import Predictions
from django.shortcuts import render, redirect, get_object_or_404
import pickle

# Define Constant
MODELFILE = settings.MODEL_DIR + '/diseaseModel.pkl'

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

def predict(request,message=None):
    inputs =COD.objects.order_by('-id').values_list('maelezo', flat=True).first()
    # row_count = all_maelezo.count()
    other_field= COD.objects.all().order_by('-id').first()
    # Check if inputs is a string
    if isinstance(inputs, str):
        # Convert inputs as a list
        inputs = [inputs]
    # Load the ML model
    with open(MODELFILE, 'rb') as f:
        model = pickle.load(f)

    # Generate prediction using the model and user inputs
    prediction = model.predict(inputs)
    
    username = request.user.username 
    return render(request, 'prediction/success.html',{'all_maelezo': inputs, 'other_field':other_field, 'username': username, 'prediction': prediction,})

def delete_questionnaire(request):
    object_to_delete = COD.objects.latest('id')
    if request.method == 'POST':
    # Delete the object
      object_to_delete.delete()
      return redirect('questionaire:submit_form')
    return render(request, 'prediction/success.html', {'object_to_delete': object_to_delete})

def save_questionnaire(request):
    object_to_save = COD.objects.latest('id')
    if request.method == 'POST':
      prediction = Predictions.objects.create(**vars(object_to_save))
      object_to_save.save()
      return redirect('questionaire:submit_form')
    return render(request, 'prediction/success.html', {'object_to_save': object_to_save})