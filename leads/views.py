from django.shortcuts import render,reverse
from .models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LeadModelForm,CustomUserCreationForm
from django.views import generic
from agents.mixins import OrganisorAndLoginRequired






class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")



class LandingPageView(generic.TemplateView):
    template_name = "landing.html"



class LeadListView(LoginRequiredMixin,generic.ListView):
    template_name = "leads/lead_list.html"
    
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)

        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False) 
            queryset = queryset.objects.filter(agent__user=user)

        return queryset     
            

    def get_context_data(self, **kwargs):
        context = super(LeadListView).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull = True)
            context.update(
            {
                "unssaigned_leads":queryset
            }
            )
        return context
    
    


class LeadDetailView(OrganisorAndLoginRequired,generic.DetailView):
    template_name = "leads/lead_detail.html"
    
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)

        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation) 
            queryset = queryset.objects.filter(agent__user=user)

        return queryset 

class LeadCreateView(OrganisorAndLoginRequired,generic.CreateView):
    template_name = "leads/lead_create.html"
    # queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")    



class LeadUpdateView(OrganisorAndLoginRequired,generic.UpdateView):
    template_name = "leads/lead_update.html"
    
    form_class = LeadModelForm
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)
    def get_success_url(self):
        return reverse("leads:lead-list")
        


class LeadDeleteView(OrganisorAndLoginRequired, generic.DeleteView):
    template_name = "leads/lead_delete.html"
    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")