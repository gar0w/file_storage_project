# files/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Image, Video, Document
from .forms import ImageForm, VideoForm, DocumentForm

def index(request):
    images = Image.objects.all()
    videos = Video.objects.all()
    documents = Document.objects.all()
    return render(request, 'files/index.html', {'images': images, 'videos': videos, 'documents': documents})

def delete_file(request, file_type, file_id):
    # Determinamos el modelo correspondiente según el tipo de archivo
    if file_type == 'image':
        model_class = Image
    elif file_type == 'video':
        model_class = Video
    elif file_type == 'document':
        model_class = Document
    else:
        # Si el tipo de archivo no es válido, lanzamos un error 404
        raise Http404("File type does not exist")

    # Intentamos obtener el objeto del modelo correspondiente con el ID proporcionado
    file = get_object_or_404(model_class, id=file_id)

    # Si el método de la solicitud es POST, procedemos con la eliminación
    if request.method == 'POST':
        file.delete()
        return redirect('index')

    # Renderizamos el template para confirmar la eliminación
    return render(request, 'files/delete_file.html', {'file': file})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image_success')
    else:
        form = ImageForm()
    return render(request, 'files/upload_image.html', {'form': form})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_video_success')
    else:
        form = VideoForm()
    return render(request, 'files/upload_video.html', {'form': form})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_document_success')
    else:
        form = DocumentForm()
    return render(request, 'files/upload_document.html', {'form': form})

def upload_image_success(request):
    return render(request, 'files/upload_image_success.html')

def upload_video_success(request):
    return render(request, 'files/upload_video_success.html')

def upload_document_success(request):
    return render(request, 'files/upload_document_success.html')
