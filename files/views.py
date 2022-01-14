import string
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.http import StreamingHttpResponse, FileResponse, HttpResponseRedirect
from django.template import loader
from wsgiref.util import FileWrapper
from django.shortcuts import redirect
from .forms import FileForm
from .models import File
from hashids import Hashids
import os


secret_key = os.getenv('SECRET_KEY', 'secret salt')
hashids = Hashids(min_length=4, salt=secret_key)

def get_file(request: HttpRequest, file_id : string):
    file_id = hashids.decode(file_id)
    file_id = file_id[0]
    file_obj: File = File.objects.get(pk=file_id)
    file = file_obj.file
    content_disposition = f'attachment; filename={os.path.basename(file.name)}'
    response = FileResponse(file)
    response['Content-Length'] = file.size
    response['Content-Disposition'] = content_disposition
    return response

def upload(request : HttpRequest):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if (form.is_valid()):
            obj : File = form.save()
            hashid = hashids.encode(obj.id)
            return HttpResponse(f'http://127.0.0.1:8000/get/{hashid}')
    return HttpResponseRedirect('/')

def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'File Drop',
    }
    return HttpResponse(template.render(context, request))
