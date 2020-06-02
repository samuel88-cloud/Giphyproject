from django.shortcuts import render
import urllib.request,json

# Create your views here.
from django.http import HttpResponse
def quill(request):
    return render(request,'quill1.html')

def addtoquill(request):
    return render(request,'quill1.html')

def index(request):
    button=0
    return render(request,'index.html')

def search(request):
    button=1
    searchstring=request.POST['imagetosearch']
    offset=0
    print(searchstring)
    url="http://api.giphy.com/v1/gifs/search?q="+str(searchstring)+"&api_key=8sj5guiBo7DEkn4tHTXEp8i7wnauKrjZ&limit=8&offset="+str(offset)
    print(url)
    #data=json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5").read())

    data=json.loads(urllib.request.urlopen(url).read())
    #print(json.dumps(data, sort_keys=True, indent=4))
    data1=data['data']
    imagedata=[]
    for i in data1:
        print(i['images']['480w_still']['url'])
        imagedata.append(i['images']['preview_gif']['url'])
    offset=offset+8
    return render(request,'index.html',{'imagedata':imagedata,'searchstring':searchstring,'offset':offset})

def next(request):
    searchstring=request.POST['searchstringfrompage']
    offset=int(request.POST['offsetfrompage'])+8
    print(searchstring)
    print(offset)
    url="http://api.giphy.com/v1/gifs/search?q="+str(searchstring)+"&api_key=8sj5guiBo7DEkn4tHTXEp8i7wnauKrjZ&limit=8&offset="+str(offset)
    print(url)
    #data=json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5").read())

    data=json.loads(urllib.request.urlopen(url).read())
    #print(json.dumps(data, sort_keys=True, indent=4))
    data1=data['data']
    imagedata=[]
    for i in data1:
        print(i['images']['480w_still']['url'])
        imagedata.append(i['images']['preview_gif']['url'])

    return render(request,'index.html',{'imagedata':imagedata,'searchstring':searchstring,'offset':offset})
