import os
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.conf import settings
from django.http import Http404

def index(request):
    return HttpResponseRedirect('https://github.com/ihptru/OpenRA-Content-Engine/wiki/Set-up-MapAPI-mirror')

def API(request, arg):
	path = settings.PATH_TO_MAPS
	listmaps = os.listdir(path)
	oramap = ""
	for item in listmaps:
		if arg in item:
			served_name = item.split(arg + "_")[1]
			if not path.endswith('/'):
				path = path + '/'
			oramap = path + item.strip()
			break
	if oramap == "":
		raise Http404
	response = StreamingHttpResponse(open(oramap), content_type='application/zip')
	response['Content-Disposition'] = 'attachment; filename = "%s"' % served_name
	return response