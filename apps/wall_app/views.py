from django.shortcuts import render, redirect
# from apps.wall_app.models import User
from .models import User, Message, Comment

# Create your views here.
def index(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'comments': Comment.objects.all(),
        'all_messages': Message.objects.all(),
        # 'messages': Message.objects.all().order_by("-created_at")
    }
    return render(request, "wall_app/wall.html", context)

def PostMessage(request):
    print("**************Posting Message****************")
    if 'id' not in request.session:
        return redirect('/wall')
    else:
        message = Message.objects.create(message=request.POST['message'], user=User.objects.get(id=request.session['id']))
        print(request.POST)
        print(f"message: {message}")
    return redirect('/wall')

def DeleteMessage(request):
    user_message = Message.objects.get(id=request.POST['message_id'])
    user_message.delete()
    return redirect('/wall')

def PostComment(request):
    if 'id' not in request.session:
        return redirect('/wall')
    else:
        print(request.POST)
        Comment.objects.create(comment=request.POST['comment'], 
        user=User.objects.get(id=request.session['id']), 
        message=Message.objects.get(id=request.POST["message_id"]))
       
    return redirect('/wall')

def DeleteComment(request):
    user_comment = Comment.objects.get(id=request.POST['comment_id'])
    user_comment.delete()
    return redirect('/wall')
    
