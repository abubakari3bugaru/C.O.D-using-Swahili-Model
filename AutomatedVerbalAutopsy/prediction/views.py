
from django.shortcuts import render, redirect
from django.conf import settings
from questionnaire.models import COD
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
    return render(request, 'prediction/success.html',{'all_maelezo': inputs, 'username': username, 'prediction': prediction,})
