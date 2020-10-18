from django.urls import reverse_lazy
from .forms import gridSliderForm
from demoapp.models import gridSlider
from django.views.generic import CreateView, ListView, UpdateView


class AddGrid(CreateView):
    model = gridSlider
    form_class = gridSliderForm
    template_name = 'gentelella/grid_slider/inputs.html'
    success_url = reverse_lazy('grid-slider-list')

   
class ListGrid(ListView):
    model= gridSlider
    template_name='gentelella/grid_slider/view_inputs.html'
    
    def get_queryset(self):
        return self.model.objects.all()
    

class UpdateGrid(UpdateView):
    model = gridSlider
    form_class = gridSliderForm
    template_name = 'gentelella/grid_slider/inputs.html'
    success_url = reverse_lazy('grid-slider-list')
