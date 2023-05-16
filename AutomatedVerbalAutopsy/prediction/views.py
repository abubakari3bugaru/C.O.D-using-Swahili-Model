
from django.shortcuts import render, redirect
from django.conf import settings
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
