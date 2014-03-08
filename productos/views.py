from django.views.generic import TemplateView
from models import Producto

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(IndexView, self).get_context_data(**kwargs)
        contexto['productos'] = Producto.objects.all()
        return contexto