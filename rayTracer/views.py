from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RayTracerForm
import subprocess
from .models import RayTracerData
import os


# Create your views here.
def index( request ):
    # return HttpResponse("Index Page")
    return render( request , 'indexRT.html')



def programa(request):
    if request.method == 'POST':
        form = RayTracerForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            ray_tracer_data = RayTracerData(
                numero_hilos=form_data['numero_hilos'],
                numerador_proporcion=form_data['numerador_proporcion'],
                denominador_proporcion=form_data['denominador_proporcion'],
                ancho_imagen=form_data['ancho_imagen'],
                muestras_por_pixel=form_data['muestras_por_pixel'],
                numerador_max_rayos=form_data['numerador_max_rayos'],
                coordenada_x=form_data['coordenada_x'],
                coordenada_y=form_data['coordenada_y'],
                coordenada_z=form_data['coordenada_z'],
                valor_R_esfera1=form_data['valor_R_esfera1'],
                valor_G_esfera1=form_data['valor_G_esfera1'],
                valor_B_esfera1=form_data['valor_B_esfera1'],
                valor_R_esfera2=form_data['valor_R_esfera2'],
                valor_G_esfera2=form_data['valor_G_esfera2'],
                valor_B_esfera2=form_data['valor_B_esfera2'],
                indice_refraccion=form_data['indice_refraccion']
            )
            ray_tracer_data.save()

            numero_hilos = request.POST.get('numero_hilos')
            numerador_proporcion = request.POST.get('numerador_proporcion')
            denominador_proporcion = request.POST.get('denominador_proporcion')
            ancho_imagen = request.POST.get('ancho_imagen')
            muestras_por_pixel = request.POST.get('muestras_por_pixel')
            numerador_max_rayos = request.POST.get('numerador_max_rayos')
            coordenada_x = request.POST.get('coordenada_x')
            coordenada_y = request.POST.get('coordenada_y')
            coordenada_z = request.POST.get('coordenada_z')
            valor_R_esfera1 = request.POST.get('valor_R_esfera1')
            valor_G_esfera1 = request.POST.get('valor_G_esfera1')
            valor_B_esfera1 = request.POST.get('valor_B_esfera1')
            valor_R_esfera2 = request.POST.get('valor_R_esfera2')
            valor_G_esfera2 = request.POST.get('valor_G_esfera2')
            valor_B_esfera2 = request.POST.get('valor_B_esfera2')
            indice_refraccion = request.POST.get('indice_refraccion')

            # Llamar al programa en C++ utilizando subprocess
            comando = ['/home/diego/Desktop/djangoproject/programa.exe', numero_hilos, numerador_proporcion, denominador_proporcion, ancho_imagen, muestras_por_pixel, numerador_max_rayos, coordenada_x, coordenada_y, coordenada_z, valor_R_esfera1, valor_G_esfera1, valor_B_esfera1, valor_R_esfera2, valor_G_esfera2, valor_B_esfera2, indice_refraccion]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            
            # Obtener la salida del programa en C++
            salida_cplusplus = resultado.stdout
            print(salida_cplusplus)

            return redirect('resultado')
            # return render(request, 'resultado.html', {'form': form})
        

    else:
        form = RayTracerForm()
    
    numero_hilos = '64'
    numerador_proporcion = '3'
    denominador_proporcion = '2'
    ancho_imagen = '400'
    muestras_por_pixel = '100'
    numerador_max_rayos = '50'
    coordenada_x = '13.0'
    coordenada_y = '2.0'
    coordenada_z = '3.0'
    valor_R_esfera1 = '1'
    valor_G_esfera1 = '1'
    valor_B_esfera1 = '1'
    valor_R_esfera2 = '1'
    valor_G_esfera2 = '1'
    valor_B_esfera2 = '1'
    indice_refraccion = '1.5'

    ruta_programa = os.path.join(os.getcwd(), 'main')

    # Llamar al programa en C++ utilizando subprocess
    comando = [ruta_programa, numero_hilos, numerador_proporcion, denominador_proporcion, ancho_imagen, muestras_por_pixel, numerador_max_rayos, coordenada_x, coordenada_y, coordenada_z, valor_R_esfera1, valor_G_esfera1, valor_B_esfera1, valor_R_esfera2, valor_G_esfera2, valor_B_esfera2, indice_refraccion]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    # Obtener la salida del programa en C++
    print(resultado.stdout, '  d')
    return render(request, 'programa.html', {'form': form})

def resultado(request):
    ray_tracer_data = RayTracerData.objects.last()  # Obtener el último objeto guardado en la base de datos

    return render(request, 'resultado.html', {'ray_tracer_data': ray_tracer_data})
