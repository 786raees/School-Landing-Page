from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import IndexPage, Program
# Create your views here.


class IndexView(TemplateView):
    template_name = "school_front/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = IndexPage.objects.first()
        programs = Program.objects.all()
        context["page"] = page
        context["programs"] = programs
        return context



class ProgramDetailView(DetailView):
    template_name = "school_front/programs/elementary.html"
    model = Program
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = IndexPage.objects.first()
        programs = Program.objects.all()
        context["page"] = page
        context["programs"] = programs
        return context

def all_templates(request, template_name):
    template_name = f"school_front/{template_name}"
    return render(request, template_name)


def all_templates_with_dir(request, template_dir, template_name):
    template_name = f"school_front/{template_dir}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir(request, template_dir1, template_dir2, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir_dir(request, template_dir1,template_dir2,template_dir3, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_dir3}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir_dir_dir(request, template_dir1, template_dir2, template_dir3, template_dir4, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_dir3}/{template_dir4}/{template_name}"
    return render(request, template_name)
