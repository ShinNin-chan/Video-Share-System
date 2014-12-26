from django.shortcuts import render_to_response

# Create your views here.
def friendManage(request):
	return render_to_response('friendManage.html')

def follow(request,master):
	pair = FriendPair()
	pair.follower = request.user
	pair.master = master
	pair.save()
	

