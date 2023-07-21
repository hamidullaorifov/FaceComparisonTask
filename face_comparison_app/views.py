from django.shortcuts import render
from django.http import HttpResponse
from .utils import are_same_person

def index(request):
    if request.method == 'POST':
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']

        result = are_same_person(image1, image2)

        return render(request, 'face_comparision_app/index.html', {'result': result})
    
    return render(request, 'face_comparision_app/index.html')
