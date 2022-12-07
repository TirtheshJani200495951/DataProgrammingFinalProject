from django.shortcuts import render, HttpResponse
import urllib, json
from home.models import Book
import pandas as pd



# Create your views here.
def index(request):
    url="https://api.opencovid.ca/summary?geo=pt&fill=true&version=true&pt_names=canonical&hr_names=canonical&fmt=json"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())
     
    return render(request, 'index.html', {'data':data})
    
def book(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        date= request.POST.get('date')
        book=Book(name=name,email=email,phone=phone,date=date)
        book.save()
    return render(request, 'book.html') 

def visualise(request):
    import urllib, json
    url="https://api.opencovid.ca/summary?geo=pt&fill=true&version=true&pt_names=canonical&hr_names=canonical&fmt=json"
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())
    data1 = (data["data"])
    data2 =  pd.DataFrame(data1)
    
    data3 = data2[['region','cases', 'deaths','hospitalizations' ]].copy()
    
    weather = data3.copy()
    title = "Monthly Max and Min Temperature"
    temps = weather[['region','cases', 'deaths','hospitalizations']]
    temps['cases'] = temps['cases']
    temps['Avg'] = (temps['cases']+temps['hospitalizations'])/2
    
    d = temps.values.tolist()
    c = temps.columns.tolist()
    d.insert(0,c)

    tempdata = json.dumps({'title':title,'data':d})	
    return render(request, 'weather.html') 
    
    
def v1(request):
        import plotly.graph_objects as go
        import plotly
        import numpy as np
        import plotly.express as px
        from django.shortcuts import redirect
        import urllib, json
        import os
        from django.conf import settings
        base_dir = settings.BASE_DIR
        path = base_dir
        print(base_dir)
        path = (os.path.join(path, "Kovid/templates"))
        print(path)
        os.chdir(path)
   
   
        url="https://api.opencovid.ca/summary?geo=pt&fill=true&version=true&pt_names=canonical&hr_names=canonical&fmt=json"
        res=urllib.request.urlopen(url)
        data=json.loads(res.read())
        data1 = (data["data"])
        data2 =  pd.DataFrame(data1)
        
        data3 = data2[['region','cases', 'deaths','hospitalizations' ]].copy()
        
        print("Library imported of the function") 
        print("################################################")
        print("plotting")
        print("#####################")
        print("###########################################")

        fig = go.Figure()


        filename='plots.html'
        import os
        #os.remove(filename)
        print("Printing the plot")
        # Plot and embed in ipython notebook!

        import plotly.express as px
        long_df = pd.DataFrame( data3)
        long_df
        fig = px.bar(long_df, x="region", y="cases", color="deaths", title="Long-Form Input")
        #fig.show()
        plotly.offline.plot(fig,  filename=filename, auto_open= False, config=dict(displayModeBar=False))
        return render(request,'plots.html')
                       
                

    



   