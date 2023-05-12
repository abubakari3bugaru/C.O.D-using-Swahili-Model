from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
# from .models import PredictionModel
import pickle
import sklearn

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        # Get user inputs
        inputs = request.POST.get('inputs')
        
        # Check if inputs is a string
        if isinstance(inputs, str):
            # Convert inputs to list of strings
            inputs = [inputs]

        # Load the saved data ML model
        with open('Models/diseaseModel.pkl', 'rb') as f:
            model = pickle.load(f)

        # Generate predictioins using the model and user inputs
        prediction = model.predict(inputs)

        # Pass the prediction to the template
        context = {'prediction': prediction}
        return render(request, 'prediction.html', context)
    else:
        return render(request, 'prediction.html')
def index(request):
    return HttpResponse("Hello, Prediction")
