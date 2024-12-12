from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		your_name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		return render(request, 'contact.html', {'message_name': your_name})
	else:
		return render(request, 'contact.html', {})


def services(request):
	return render(request, 'services.html')


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['email']
		your_phone = request.POST['your-number']
		your_date = request.POST['choose-date']
		your_time = request.POST['choose-time']
		your_issue = request.POST['your-issue']

		return render(request, 'appointmentresult.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_phone': your_phone,
			'your_date': your_date,
			'your_time': your_time,
			'your_issue': your_issue
			})
	else:
		return render(request, 'appointment.html')


def about(request):
	return render(request, 'about.html')


def appointmentresult(request):
	return render(request, 'appointmentresult.html')