from django.http import Http404

def get_form(request, FormClass):
	if request.method != 'POST':
		raise Http404('Invalid request.')
	f = FormClass(request.POST)
	if not f.is_valid():
		raise Http404('Invalid form.')
	return f

def get_new_task_id(username):
	previous_tasks = Task.objects.filter(username=username)
	if previous_tasks:
		return max(t.task_id for t in previous_tasks) + 1
	else:
		return 1

def get_new_task_order(username, project):
	previous_tasks = Task.objects.filter(username=username, project=project)
	ids = [t.order for t in previous_tasks]
	if not project:
		ids += [p.order for p in Project.objects.all()]
	if ids:
		return max(ids) + 1
	else:
		return 1

def time_string(seconds):
	h = int(seconds // 3600)
	m = int(seconds // 60 % 60)
	s = int(seconds % 60)
	time_str = "<b>{0:02}</b> M <b>{1:02}</b> S".format(m,s)
	if h != 0:
		time_str = "<b>{}</b> H ".format(h) + time_str
	return time_str
