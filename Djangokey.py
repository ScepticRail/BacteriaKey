from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	
	if request.GET.has_key('grampos'): # if a button has been pressed
		
		if request.GET['grampos'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/cat/")

		elif request.GET['grampos'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/ox/")

	buttons = '<a href="/?grampos=Y"><button>Yes</button></a>'+ '<a href="/?grampos=N"><button>No</button></a>'
	
	question = "Is your bacterium Gram-positive?" 

	output = buttons + question
	
	return HttpResponse(output) # shove the contents of output into an HTML document and return that


def cat(request):
	
	if request.GET.has_key('cat'): # if a button has been pressed
		
		if request.GET['cat'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/coag/")

		elif request.GET['cat'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/aghaemo/")

	buttons = '<a href="/cat/?cat=Y"><button>Yes</button></a>'+ '<a href="/cat/?cat=N"><button>No</button></a>'
	
	question = "Is your bacterium catalase-positive?" 

	output = buttons + question
	
	return HttpResponse(output) 

def coag(request):

	if request.GET.has_key('coag'): # if a button has been pressed
		
		if request.GET['coag'] == "Y": # and that button was YES, do
	
			return HttpResponse("Your bacterium is STAPHYLOCOCCUS AUREUS.")

		elif request.GET['coag'] == "N": # and that button was NO, do
			return HttpResponse("Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS.")

	buttons = '<a href="/coag/?coag=Y"><button>Yes</button></a>'+ '<a href="/coag/?coag=N"><button>No</button></a>'
	
	question = "Is your bacterium coagulase-positive?" 

	output = buttons + question
	
	return HttpResponse(output)

def aghaemo(request):
	
	if request.GET.has_key('aghaemo'): # if a button has been pressed
		
		if request.GET['aghaemo'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/esc/")

		elif request.GET['aghaemo'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/bhaemo/")

	buttons = '<a href="/aghaemo/?aghaemo=Y"><button>Yes</button></a>'+ '<a href="/aghaemo/?aghaemo=N"><button>No</button></a>'
	
	question = "Does your bacterium exhibit alpha or gamma haemolysis?" 

	output = buttons + question
	
	return HttpResponse(output)


def esc(request):
	
	if request.GET.has_key('esc'): # if a button has been pressed
		
		if request.GET['esc'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/opt/")

		elif request.GET['esc'] == "N": # and that button was NO, do
			return HttpResponse("Your bacterium is ENTEROCCOCUS FAECALIS.")

	buttons = '<a href="/esc/?esc=Y"><button>Yes</button></a>'+ '<a href="/esc/?esc=N"><button>No</button></a>'
	
	question = "Is your bacterium capable of hydrolising esculin in the presence of bile?" 

	output = buttons + question
	
	return HttpResponse(output) 

def opt(request):
	
	if request.GET.has_key('opt'): # if a button has been pressed
		
		if request.GET['opt'] == "Y": # and that button was YES, do
	
			return HttpResponse("Your bacterium is STREPTOCOCCUS MITIS.")

		elif request.GET['opt'] == "N": # and that button was NO, do
			return HttpResponse("Your bacterium is STREPTOCOCCUS PNEUMONIAE.")

	buttons = '<a href="/opt/?opt=Y"><button>Yes</button></a>'+ '<a href="/opt/?opt=N"><button>No</button></a>'
	
	question = "Is your bacterium optochin-resistant?" 

	output = buttons + question
	
	return HttpResponse(output) 

def bhaemo(request):
	
	if request.GET.has_key('bhaemo'): # if a button has been pressed
		
		if request.GET['bhaemo'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/camp/")

		elif request.GET['bhaemo'] == "N": # and that button was NO, do
			return HttpResponse("I don't know what this organism is.")

	buttons = '<a href="/aghaemo/?bhaemo=Y"><button>Yes</button></a>'+ '<a href="/bhaemo/?bhaemo=N"><button>No</button></a>'
	
	question = "Does your bacterium exhibit beta haemolysis?" 

	output = buttons + question
	
	return HttpResponse(output)

def camp(request):
	
	if request.GET.has_key('camp'): # if a button has been pressed
		
		if request.GET['camp'] == "Y": # and that button was YES, do
	
			return HttpResponse("Your bacterium is STREPTOCOCCUS AGALACTIAE.")

		elif request.GET['camp'] == "N": # and that button was NO, do
			return HttpResponse("Your bacterium is STREPTOCOCCUS PYOGENES.")

	buttons = '<a href="/camp/?camp=Y"><button>Yes</button></a>'+ '<a href="/camp/?camp=N"><button>No</button></a>'
	
	question = "Does your organism express the CAMP factor?" 

	output = buttons + question
	
	return HttpResponse(output)

##### GRAM NEGATIVE BULLSHIT #####
def ox(request):
	
	if request.GET.has_key('ox'): # if a button has been pressed
		
		if request.GET['ox'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/nit/")

		elif request.GET['ox'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/lac/")

	buttons = '<a href="/ox/?ox=Y"><button>Yes</button></a>'+ '<a href="/ox/?ox=N"><button>No</button></a>'
	
	question = "Is your bacterium oxidase-positive?" 

	output = buttons + question
	
	return HttpResponse(output) 

def nit(request):
	
	if request.GET.has_key('nit'): # if a button has been pressed
		
		if request.GET['nit'] == "Y": # and that button was YES, do
	
			return HttpResponse("Your bacterium is PSEUDOMONAS AERUGINOSA.")

		elif request.GET['nit'] == "N": # and that button was NO, do
			return HttpResponse("Your bacterium is ALCALIGENES FAECALIS.")

	buttons = '<a href="/nit/?nit=Y"><button>Yes</button></a>'+ '<a href="/nit/?nit=N"><button>No</button></a>'
	
	question = "Is your bacterium nitratase-positive?" 

	output = buttons + question
	
	return HttpResponse(output) 

def lac(request):
	
	if request.GET.has_key('lac'): # if a button has been pressed
		
		if request.GET['lac'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/dur/")

		elif request.GET['lac'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/mot/")

	buttons = '<a href="/lac/?lac=Y"><button>Yes</button></a>'+ '<a href="/lac/?lac=N"><button>No</button></a>'
	
	question = "Is your bacterium capable of fermenting lactose?" 

	output = buttons + question
	
	return HttpResponse(output)

def dur(request):
	
	if request.GET.has_key('dur'): # if a button has been pressed
		
		if request.GET['dur'] == "Y": # and that button was YES, do
	
			return HttpResponseRedirect("/dur/")

		elif request.GET['dur'] == "N": # and that button was NO, do
			return HttpResponseRedirect("/mot/")

	buttons = '<a href="/dur/?dur=Y"><button>Yes</button></a>'+ '<a href="/dur/?dur=N"><button>No</button></a>'
	
	question = "Is your bacterium hydrogen lyase-positive?" 

	output = buttons + question
	
	return HttpResponse(output)
