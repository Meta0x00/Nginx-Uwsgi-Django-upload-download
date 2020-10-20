from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")


def upload_file(request,uid):
    if request.method == 'POST':
        myFile = request.FILES.get("myfile",None)
        if not myFile:
            return HttpResponse('no files for upload!')

        Product.objects.filter(id=uid).update(image=myFile.name,jad_address=myFile)
        destination = open(os.path.join("/root/django/server/server/upload",myFile.name),'wb+')

        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return redirect('/index/')
