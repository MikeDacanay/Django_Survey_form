from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	return render(request,'survey/index.html')

def result(request):
	return render(request,'survey/result.html')	

def process(request):
	request.session["name"]=request.POST['name_form']
	request.session['lang']=request.POST['lang_form']
	request.session['loc']=request.POST['loc_form']
	request.session['comment']=request.POST['comment_form']
	if 'counter' not in request.session:
		request.session['counter']=0
	request.session['counter']+=1
	return redirect('/survey/result')

# def process(request):

