<<<<<<< HEAD
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io



def fonct(request):
    return render(request, 'index.html')



# Charger le modèle une seule fois lors du démarrage du serveur
model = load_model('fake_real_classifier_model.h5')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return JsonResponse({'error': 'No image uploaded'}, status=400)

        # Lire l'image de la requête
        image_file = request.FILES['image']
        img = Image.open(image_file)

        # Préparer l'image pour le modèle
        img = img.resize((150, 150))  # Redimensionner l'image
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Faire une prédiction
        prediction = model.predict(img_array)
        result = 'Real' if prediction[0][0] > 0.5 else 'Fake'

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
=======
from django.shortcuts import render
from django.http import HttpResponse


def fonct(request):
    return render(request, 'index.html')
>>>>>>> 1409d30141be0c20f2e435566dfc041b20f24adf
