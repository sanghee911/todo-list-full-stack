from django.views.generic import TemplateView
import os
import socket


class IndexTemplateView(TemplateView):
    template_name = "index.html"
    frontend_ip = os.environ.get('FRONTEND_IP', 'localhost:8080')
    pgadmin_ip = os.environ.get('PGADMIN_IP', 'localhost:8001')

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['frontend_ip'] = self.frontend_ip
        context['hostname'] = socket.gethostname()
        context['pgadmin_ip'] = self.pgadmin_ip
        return context
