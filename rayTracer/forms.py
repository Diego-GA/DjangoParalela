from django import forms

class RayTracerForm(forms.Form):
    numero_hilos = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numerador_proporcion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    denominador_proporcion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ancho_imagen = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    muestras_por_pixel = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numerador_max_rayos = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    coordenada_x = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    coordenada_y = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    coordenada_z = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_R_esfera1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_G_esfera1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_B_esfera1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_R_esfera2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_G_esfera2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor_B_esfera2 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    indice_refraccion = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # proporcion = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # ancho = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # muestras = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # rayos = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # coordenadas = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # color = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # indice_refraccion = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))

