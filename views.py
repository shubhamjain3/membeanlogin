from .forms import UploadFileForm
from django.contrib import auth
from django.shortcuts import render,HttpResponseRedirect
import uuid
from django.core.exceptions import ObjectDoesNotExist


from .forms import EmailForm,NameForm,JoinForm,LoginForm
from .models import join,uploads


#def share(request,ref_id):
    

 #       joined = join.objects.get(ref_id=ref_id)

  #      context={'ref_id':ref_id,'f_name':joined.f_name,'l_name':joined.l_name}
   #     template='share.html'
    #    return render(request,template,context)


def get_ref_id():
    ref_id=str(uuid.uuid4())[:11].replace('-','').upper()
    return ref_id
def home(request):
#    form1=EmailForm(request.POST or None)
 #   form2=NameForm(request.POST or None)
  #  if form1.is_valid():
   #     email=form1.cleaned_data['email']
    #    new_join,created=join.objects.get_or_create(email=email)
     #   print new_join,created
#    if form2.is_valid():
 #       f_name=form2.cleaned_data['f_name']
  #      l_name=form2.cleaned_data['l_name']
   #     created=join.objects.get_or_create(f_name=f_name)
    #    created=join.objects.get_or_create(l_name=l_name)
    form =JoinForm(request.POST or None)
    if form.is_valid():
        new_join=form.save(commit=False)
        email=form.cleaned_data['email']
        f_name=form.cleaned_data['f_name']
        l_name=form.cleaned_data['l_name']

        
        new_join_old,created=join.objects.get_or_create(email=email)
        if created:
            new_join_old.f_name=f_name
            new_join_old.l_name=l_name
            new_join_old.ref_id=get_ref_id()
            new_join_old.save()
        
        return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
    context={'form':form}
        
    return render(request,'home.html',context)
       
def upload_file(request):
    saved=False
    if request.method == 'POST':
        uform = UploadFileForm(request.POST, request.FILES)
        if uform.is_valid():
            uploads=uploads()
            uploads.name=uform.cleaned_data["title"]
            uploads.file=uform.cleaned_data["file"]
            uploads.save()
            saved=True

            
    else:
        uform = UploadFileForm()
    return render(request, 'upload.html', {'uform': uform})
