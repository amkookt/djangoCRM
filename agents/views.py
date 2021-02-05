from django.views import  generic
from leads.models import Agent
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequired






class AgentCreateView(OrganisorAndLoginRequired,generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.save()
        Agent.objects.create(
            user=user, 
            organisation=self.request.user.userprofile

        )
        return super(AgentCreateView,self).form_valid(form)    
    



class AgentListView(OrganisorAndLoginRequired,generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    



class AgentDetailView(OrganisorAndLoginRequired,generic.DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = "agent"
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)



class AgentUpdateView(OrganisorAndLoginRequired,generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    def get_queryset(self):
        return Agent.objects.all()
    def get_success_url(self):
        return reverse("agents:agent-list")    
    



class AgentDeleteView(OrganisorAndLoginRequired,generic.DeleteView):
    template_name = "agents/agent_delete.html"
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")