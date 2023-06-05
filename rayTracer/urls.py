from django.urls import path
from . import views




urlpatterns = [
    path(''      ,                      views.index, name='indexRT'),
    path('about/',                      views.programa, name="programa"),
    path('resultado/',                      views.resultado, name="resultado"),


    # path('hello/<str:username>',        views.hello),
    # path('projects/',                   views.projects),
    # path('tasks/'  ,                    views.tasks)
    # path('tasks/<int:id>',                  views.tasks),
]