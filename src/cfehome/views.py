import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit
this_dir=pathlib.Path(__file__).resolve().parent

def home_view(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)

def about_view(request,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    try:
              
        
        percent=(page_qs.count()*100.0)/qs.count(),

    except:
        percent=0    
    my_title="My Page"
    html_template="home.html"

    my_context={
        "page_title":my_title,
        "page_visits_count":page_qs.count(),
        "percent":(page_qs.count()*100.0)/qs.count(),
        "total_visits":qs.count()
    }
    
    path=request.path
  
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    #html_file_path=this_dir/"home.html"
   # html_=html_file_path.read_text()

    return render(request,html_template,my_context)
def home_page_view_old (request,*args,**kwargs):
    my_title="My Page"

    my_context={
        "page_title":my_title
    }
  
    html_="""
<!DOCTYPE html>
<html>

<body>
<h1>{page_title}Inline is anything</h1>
</body>

    </html>
""".format(**my_context)
    #html_file_path=this_dir/"home.html"
   # html_=html_file_path.read_text()

    return HttpResponse(html_)
    
  
  
