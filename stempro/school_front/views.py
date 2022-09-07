from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "school_front/index.html"

def all_templates(request, template_name):
    template_name = f"school_front/{template_name}"
    return render(request, template_name)


def all_templates_with_dir(request, template_dir, template_name):
    template_name = f"school_front/{template_dir}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir(request, template_dir1, template_dir2, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_name}"
    return render(request, template_name)
