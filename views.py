from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import QuizForm
from .models import quiz
def disp(request):
    msg1="answer is true"
    msg2="answer is wrong"
    form=QuizForm(request.POST or None)
    if form.is_valid():
        print form.cleaned_data['userans']
        userans=form.cleaned_data['userans']
        old=quiz.objects.get(s_no='1')
        print old.s_no
        
        if userans==old.ans:
            context={'msg':msg1,'form':form}
        else:
            context={'msg':msg2,'form':form}
    else:
        form=QuizForm()
        

  
    return render(request,'quiz_disp.html',context)

    
    
