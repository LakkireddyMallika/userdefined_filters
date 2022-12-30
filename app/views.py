from django.shortcuts import render



# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'hi My name is MALLIKA','dt':dt,'c':2}
    return render(request,'filters.html',d)


def userdefinedfilters(request):
    d={'data':'MaLLika'}
    return render(request,'userdefinedfilters.html',d)