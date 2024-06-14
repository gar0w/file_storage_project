from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página principal que lista todos los archivos
    path('upload/image/', views.upload_image, name='upload_image'),  # Formulario de carga de imágenes
    path('upload/video/', views.upload_video, name='upload_video'),  # Formulario de carga de videos
    path('upload/document/', views.upload_document, name='upload_document'),  # Formulario de carga de documentos
    path('upload/image/success/', views.upload_image_success, name='upload_image_success'),  # Confirmación de carga de imágenes
    path('upload/video/success/', views.upload_video_success, name='upload_video_success'),  # Confirmación de carga de videos
    path('upload/document/success/', views.upload_document_success, name='upload_document_success'),  # Confirmación de carga de documentos
    path('delete/<str:file_type>/<int:file_id>/', views.delete_file, name='delete_file'), # URL para eliminar archivos
]
