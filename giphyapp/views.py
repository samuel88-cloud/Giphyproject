from django.shortcuts import render
import urllib.request,json

# updated views
from django.http import HttpResponse
def quill(request):
    return render(request,'quill.html')

def addtoquill(request,image):
    print('inside addtoquill')
    imageurl=image
    print(imageurl)
    return render(request,'quill.html',{'imageurl':imageurl})

def searchindex(request):
    print('inside index')
    return render(request,'searchindex.html')

def search(request):
    print('inside search')

    searchstring=request.POST['imagetosearch']
    searchstring="".join(searchstring.split()) 
    offset=0
    print(searchstring)
    url="http://api.giphy.com/v1/gifs/search?q="+str(searchstring)+"&api_key=8sj5guiBo7DEkn4tHTXEp8i7wnauKrjZ&limit=18&offset="+str(offset)
    print(url)
    #data=json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5").read())

    data=json.loads(urllib.request.urlopen(url).read())
    #print(json.dumps(data, sort_keys=True, indent=4))
    data1=data['data']
    imagedata=[]
    for i in data1:
        print(i['images']['480w_still']['url'])
        imagedata.append(i['images']['preview_gif']['url'])
    return render(request,'searchindex.html',{'imagedata':imagedata,'searchstring':searchstring,'offset':offset})

def next(request):
    searchstring=request.POST['searchstringfrompage']
    offset=int(request.POST['offsetfrompage'])+18
    print(searchstring)
    print(offset)
    url="http://api.giphy.com/v1/gifs/search?q="+str(searchstring)+"&api_key=8sj5guiBo7DEkn4tHTXEp8i7wnauKrjZ&limit=18&offset="+str(offset)
    print(url)
    #data=json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5").read())

    data=json.loads(urllib.request.urlopen(url).read())
    #print(json.dumps(data, sort_keys=True, indent=4))
    data1=data['data']
    imagedata=[]
    for i in data1:
        print(i['images']['480w_still']['url'])
        imagedata.append(i['images']['preview_gif']['url'])

    return render(request,'searchindex.html',{'imagedata':imagedata,'searchstring':searchstring,'offset':offset})
