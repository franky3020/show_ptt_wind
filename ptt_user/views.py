from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import datetime

from .mysql_select_from_ptt import ptt_user_name



def user_name_page(request):
    
    if 'user_name' in request.GET:
        if('msg_like' in request.GET):
            
            if request.GET['msg_like'] != "":
                msg_like = request.GET['msg_like']
            else:
                msg_like = None 
                
        else:
            msg_like = None
        
        return render(request, 'user_name_page.html', {
        'msg_list': ptt_user_name(request.GET['user_name'],msg_like),
        })
        
    else:
        return render(request, 'user_name_page.html')

def key_word_search(request):
    pass
        


