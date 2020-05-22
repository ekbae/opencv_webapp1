from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage

def first_view(request):
    return render(request, 'opencv_web/first_view.html',{})

def uimage(request): # when writing
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile=request.FILES['image']
            fs = FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
            uploaded_file_url=fs.url(filename)
            return render(request, 'opencv_web/uimage.html',
                      {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:# when no writing, on here
        form=UploadImageForm()
        return render(request, 'opencv_web/uimage.html',
                      {'form': form})
