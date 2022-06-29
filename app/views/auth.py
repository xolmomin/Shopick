from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from app.forms import RegistrationForm
from app.forms import UserModelForm


class LoginPage(TemplateView):
    template_name = 'app/login.html'


class RegisterPage(FormView):
    # form_class = RegistrationForm
    # success_url = reverse_lazy('login')
    template_name = 'app/register.html'

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


#
# def register_page(request):
#     form = RegistrationForm()
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#
#     return render(request,'app/register.html',{'form':form})






class MyAccPage(TemplateView):
    template_name = 'app/my-account.html'
