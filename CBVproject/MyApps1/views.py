from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from MyApps1.models import Book
from django.views.generic import ListView
from django.shortcuts import render
from MyApps1.models import Company
from django.views.generic import DetailView, ListView
from MyApps1.models import Company
from django.views.generic import CreateView




class HelloWorldView(View):
    def get(self,request):
        ss='''<h1>Hello from Class-Bassed-View</h1>
        <hr />
        <h2>Response given for get-method from client</h2>
        <h3>Have a nice day..!!</h3>
		<hr />
        <h4>***ALL THE BEST***</h4>
        '''
        return HttpResponse(ss)




class TemplateCBV(TemplateView):
  template_name = "MyApps1/home.html"




def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = 'Sai'
		context['age'] = 23
		context['height'] = 6.2
		return context;




class BookListView(ListView):
	context_object_name = 'books'
	model=Book;
	template_name = 'MyApps1/books.html'



class CompanyListView(ListView):
	model=Company
	#company_list = Company.objects.all();
	#default template_name is company_list.html
	#defult context_object_name is company_list var
	#{{name}} {{loc}} {{ceo}}



class CompanyDetailView(DetailView):
	model=Company
	#default template_name is company_detail.html
	#defult context_object_name is "company" or given-object for company_list, which is in usage for company_list.html


class CompanyCreateView(CreateView):
	model=Company
