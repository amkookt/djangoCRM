from django.views import  generic
from leads.models import Agent
from django.contrib.auth.mixins import LoginRequiredMixin






class AgentCreateView(LoginRequiredMixin,generic.CreateView):
    pass



class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self):
        return Agent.objects.all()
    



class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    pass



class AgentUpdateView(LoginRequiredMixin,generic.UpdateView):
    pass



class AgentDeleteView(LoginRequiredMixin,generic.DeleteView):
    pass