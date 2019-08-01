from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import Details


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Details
    template_name = 'search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Details.objects.filter(
            Q(name__icontains=query) | Q(state_id__icontains=query)
        )
        return object_list