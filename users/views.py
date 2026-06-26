from django.views.generic.base import TemplateView
from django.views.generic import CreateView,DeleteView,DetailView

# Create your views here.
class ViewUserPage(TemplateView):
    template_name ='user_temp/user_page.html'


class CreateUserPage(CreateView):
    template_name='user_temp/create_user.html'