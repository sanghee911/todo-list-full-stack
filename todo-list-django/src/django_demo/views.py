from django.views.generic import TemplateView
import os


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    try:
        frontend_ip = os.environ['FRONTEND_IP']
    except:
        frontend_ip = 'localhost'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['frontend_ip'] = self.frontend_ip
        return context
