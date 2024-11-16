from django.shortcuts import render
from django.views import View


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_based_view.html')


def functionBasedView(request):
    return render(request, 'second_task/function_based_view.html')


from django.shortcuts import render

# Create your views here.
