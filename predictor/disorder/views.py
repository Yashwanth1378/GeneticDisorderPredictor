from django.shortcuts import render
import joblib
import numpy as np

# Load model and encoders
model = joblib.load('disorder/model.pkl')
encoders = joblib.load('disorder/encoders.pkl')

def home(request):
    return render(request, 'index.html')  # FIXED: Use the correct template

def predict(request):
    if request.method == 'POST':
        try:
            mat_gene = request.POST['Maternal gene'].strip()
            pat_gene = request.POST['Paternal gene'].strip()
            blood_count = float(request.POST['Blood cell count (mcL)'])
            birth_asphyxia = request.POST['Birth asphyxia'].strip()
            maternal_illness = request.POST['H/O serious maternal illness'].strip()

            # Validate blood cell count range
            if blood_count < 3.0 or blood_count > 6.5:
                return render(request, 'index.html', {'error': 'Blood cell count must be between 3.0 and 6.5 mcL.'})

            try:
                mat_gene_encoded = encoders['Maternal gene'].transform([mat_gene])[0]
                pat_gene_encoded = encoders['Paternal gene'].transform([pat_gene])[0]
                birth_asphyxia_encoded = encoders['Birth asphyxia'].transform([birth_asphyxia])[0]
                maternal_illness_encoded = encoders['H/O serious maternal illness'].transform([maternal_illness])[0]
            except Exception as e:
                return render(request, 'index.html', {'error': f'Encoding error: {str(e)}'})

            input_data = np.array([[mat_gene_encoded, pat_gene_encoded, blood_count, birth_asphyxia_encoded, maternal_illness_encoded]])
            prediction = model.predict(input_data)[0]

            return render(request, 'result.html', {'prediction': prediction})
        except Exception as e:
            return render(request, 'index.html', {'error': f'Unexpected error: {str(e)}'})
