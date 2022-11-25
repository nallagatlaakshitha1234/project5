from django.shortcuts import render

# Create your views here.
def akshi(request):
    d={'a':200,'b':350,'c':800,'d':900}
    return render(request,'akshi.html',context= d )
