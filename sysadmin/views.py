# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budget.settings")


# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


from django.shortcuts import render_to_response
from django.http import  Http404, HttpResponseRedirect, HttpResponse

from sysadmin.models import *
from datetime import *

from django.db.models import Max,Sum




def index(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		try:			
			user=Userprofile.objects.get(email=email,password=password)
			request.session['userid'] = user.email
			varuser = request.session['userid']
			return  HttpResponseRedirect('/dashboard/')
		except:
			return HttpResponseRedirect('/login/')

	else:
		return render_to_response('dashboard.html')
		# return render_to_response('login.html')

def login(request):
	if request.method=='POST':
		email=request.POST['email']
		password=request.POST['password']
		try:			
			user=Userprofile.objects.get(email=email,password=password)
			request.session['userid'] = user.email
			varuser = request.session['userid']
			return  HttpResponseRedirect('/dashboard/')
		except:
			return HttpResponseRedirect('login.html')

	else:
		# return render_to_response('index.html')
		return render_to_response('login.html')

def dashboard(request):
	# if 'userid' in request.session:
		# varuser = request.session['userid']	
		# staff = Userprofile.objects.get(email=varuser,status=1)
		# staffdet=staff.staffrec.id
		# branch=staff.branch.id
		# mycompany=staff.branch.company
		# company=mycompany.name
		# comp_code=mycompany.id
		# ourcompay=tblCOMPANY.objects.get(id=comp_code)
		# mybranch=tblBRANCH.objects.get(company=ourcompay,id=branch)
		# staff = Userprofile.objects.filter(email=varuser,status=1)
	return render_to_response('dashboard.html')#,{'user':varuser,'company':mybranch,'menu':staff})
	# else:
	# 	return HttpResponseRedirect('/login/')


def setincome(request):
	# income=tblincome.objects.filter(month='January',year = '2020')
	if request.method=='POST':
		year=request.POST['year']
		month= request.POST['month']
		description = request.POST['description']
		amount=request.POST['amount']
		datee= date.today()
		timee =datetime.now()
		timee=timee.strftime("%H:%M:%S")

		tblincome(year=year,timee=timee,datee=datee,month=month,description=description,amount=amount).save()
		msg='INCOME SAVED SUCCESSFULLY'

	else:
		msg =''
	return render_to_response('sysadmin/income.html',{'msg':msg})

def myincome(request):
    if request.is_ajax():
    	if request.method == 'POST':
    		post = request.POST.copy()
    		acccode = post['userid']
    		state=acccode
    		year,month= acccode.split(':')
    		myincome=tblincome.objects.filter(year=year,month=month)
    		return render_to_response('sysadmin/incomeajax.html',{'income':myincome,'year':year,'month':month})
    	else:
    		return HttpResponseRedirect('/login/')
    else:
    	return HttpResponseRedirect('/login/')


def editmyincome(request):
	if request.is_ajax():
		if request.method == 'POST':
			post = request.POST.copy()
			acccode = post['userid']
			state=acccode
			myqst=tblincome.objects.get(id=acccode)
			return render_to_response('sysadmin/editincome.html',{'data':myqst})
		else:
			return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')

def change(request,vid):

	if request.method== 'POST':
		description=request.POST['descr']
		amount=request.POST['amt']
		inco= tblincome.objects.get(id=vid)
		inco.description=description
		inco.amount=amount
		inco.save()
		return HttpResponseRedirect('/sysadmin/income/')



def deletedate(request,vid):

	if request.method== 'POST':
		description=request.POST['descr']
		amount=request.POST['amt']
		inco= tblincome.objects.get(id=vid).delete()
		return HttpResponseRedirect('/sysadmin/income/')



















def budget(request):
	if request.method=='POST':
		year=request.POST['year']
		month= request.POST['month']
		description = request.POST['description']
		amount=request.POST['amount']
		datee= date.today()
		timee =datetime.now()
		timee=timee.strftime("%H:%M:%S")

		tblbudget(year=year,timee=timee,datee=datee,month=month,description=description,amount=amount).save()
		msg='INCOME SAVED SUCCESSFULLY'

	else:
		msg =''
	return render_to_response('sysadmin/budget.html',{'msg':msg})



def mybudget(request):
    if request.is_ajax():
    	if request.method == 'POST':
    		post = request.POST.copy()
    		acccode = post['userid']
    		state=acccode
    		year,month= acccode.split(':')
    		mybug=tblbudget.objects.filter(year=year,month=month)
    		return render_to_response('sysadmin/budgetajax.html',{'bdata':mybug,'year':year,'month':month})
    	else:
    		return HttpResponseRedirect('/login/')
    else:
    	return HttpResponseRedirect('/login/')


def editmybudget(request):
	if request.is_ajax():
		if request.method == 'POST':
			post = request.POST.copy()
			acccode = post['userid']
			state=acccode
			bugbug=tblbudget.objects.get(id=acccode)
			return render_to_response('sysadmin/editbudget.html',{'gdata':bugbug})
		else:
			return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')

def bugchange(request,vid):

	if request.method== 'POST':
		description=request.POST['descr']
		amount=request.POST['amt']
		inco= tblbudget.objects.get(id=vid)
		inco.description=description
		inco.amount=amount
		inco.save()
		return HttpResponseRedirect('/sysadmin/budget/')



def deletebug(request,vid):

	if request.method== 'POST':
		description=request.POST['descr']
		amount=request.POST['amt']
		inco= tblbudget.objects.get(id=vid).delete()
		return HttpResponseRedirect('/sysadmin/budget/')



def revent(request):
	if request.method=='POST':
		return HttpResponseRedirect('/sysadmin/event')# render_to_response('sysadmin/event.html')


























def setevent(request):
	msg=''
	return render_to_response('sysadmin/event.html',{'msg':msg})



def myevent(request):
    if request.is_ajax():
    	if request.method == 'POST':
    		post = request.POST.copy()
    		acccode = post['userid']
    		state=acccode
    		year,month= acccode.split(':')
    		allevent=[]
    		myevent=tblbudget.objects.filter(year=year,month=month)

    		for k in myevent:
    			bug = k.amount
    			eventt = tblevents.objects.filter(budget=k)
    			add=eventt.aggregate(Sum('amount'))
    			add = add['amount__sum']

    			bal =  bug 
    			lk = {'event':eventt,'budget':k,'total':add,'bal':bal}
    			allevent.append(lk)


    		return render_to_response('sysadmin/eventajax.html',{'allevent':allevent, 'data1':myevent,'year':year,'month':month})
    	else:
    		return HttpResponseRedirect('/login/')
    else:
    	return HttpResponseRedirect('/login/')


def editmyevent(request):
	if request.is_ajax():
		if request.method == 'POST':
			post = request.POST.copy()
			acccode = post['userid']
			state=acccode
			myqst=tblbudget.objects.get(id=acccode)
			return render_to_response('sysadmin/addexp.html',{'gdata':myqst})
		else:
			return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')

def addevent(request,vid):

	if request.method== 'POST':
		description=request.POST['description']
		amount=request.POST['amount']
		datee= date.today()
		timee =datetime.now()
		timee=timee.strftime("%H:%M:%S")

		inco= tblbudget.objects.get(id=vid)
		tblevents(description=description,amount=amount,datee=datee,
			timee=timee,budget=inco,month=datee.month).save()
		return HttpResponseRedirect('/sysadmin/event/')



def deletebug(request,vid):

	if request.method== 'POST':
		description=request.POST['descr']
		amount=request.POST['amt']
		inco= tblbudget.objects.get(id=vid).delete()
		return HttpResponseRedirect('/sysadmin/budget/')


def expenses(request):
	if request.is_ajax():
		if request.method == 'POST':
			post = request.POST.copy()
			acccode = post['userid']
			state=acccode
			myqst=tblevents.objects.get(id=acccode)
			return render_to_response('sysadmin/editevent.html',{'gdata':myqst})
		else:
			return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')


def editexpen(request,vid):

	if request.method== 'POST':
		description=request.POST['description']
		amount=request.POST['amount']
		datee= date.today()
		timee =datetime.now()
		timee=timee.strftime("%H:%M:%S")

		inco= tblevents.objects.get(id=vid)
		inco.description=description
		inco.amount=amount
		inco.save()
		# tblevents(description=description,amount=amount,datee=datee,
			# timee=timee,budget=inco,month=datee.month).save()
		return HttpResponseRedirect('/sysadmin/event/')

def delexpen(request,vid):

	if request.method== 'POST':
		description=request.POST['description']
		amount=request.POST['amount']
		datee= date.today()
		timee =datetime.now()
		timee=timee.strftime("%H:%M:%S")

		inco= tblevents.objects.get(id=vid).delete()

		return HttpResponseRedirect('/sysadmin/event/')