from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response


birthdays = {
	'john': '01.01.1991',
	'jane': '02.02.1992',
	'joe':	'03.03.1993',
	'joe1':	'03.03.1993'
}


# Create your views here.
def name_view(request, name):
	try:
		return render_to_response('birthdays/name.html',
			{
				'name': name,
				'date': birthdays[name]
			}
		)
	except KeyError:
		raise Http404('Name not found')


def birthday_view(request, birthday):
	people = []
	for key in birthdays.keys():
		if birthdays[key] == birthday:
			people.append(key)

	if len(people) > 0:
		return render_to_response('birthdays/birthday.html',
			{
				'people': people
			}
		)
	else:
		raise Http404('Any matches')
