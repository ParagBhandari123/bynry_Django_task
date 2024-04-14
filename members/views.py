from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def hell(request):
    return render(request, 'members\index.html')

def contact(request):
    return render(request, 'members\contact.html')


from django.shortcuts import  redirect
from .models import Contact

def hello_world(request):
    return HttpResponse("Hello, World!")

def hell(request):
    return render(request, 'members/index.html')

def start(request):
    return render(request, 'members/start.html')

# def home(request):
#     return render(request, 'members/home.html')

def fail(request):
    return render(request, 'members/fail.html')
def make(request):
    return render(request, 'members/make.html')

def detailsform(request):
    return render(request, 'members/detailsform.html')




def maker(request):
    return render(request, 'members/maker.html')


def display(request):
    # Retrieve all objects from the Contact model
    contacts = Contact.objects.all()
    # Pass the contacts data to the template for rendering
    return render(request, 'members/display.html', {'contacts': contacts})

from .models import ServiceRequest



def home(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'members/home.html', {'service_requests': service_requests})



def detailsform(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        name = request.POST.get('name')
        address = request.POST.get('address')
        contactnum = request.POST.get('contactnum')
        attachment = request.FILES.get('attachment')

        service_request = ServiceRequest.objects.create(id_number=id_number, name=name, address=address, contactnum=contactnum, attachment=attachment)

        # Pass the created service_request object to the home.html template
        return render(request, 'members/home.html', {'service_request': service_request})

    return render(request, 'members/detailsform.html')

# Add a new view to display detailed information
def check_info(request):
    if request.method == 'GET':
        # Retrieve the parameters from the query string
        id_number = request.GET.get('id_number')
        name = request.GET.get('name')
        address = request.GET.get('address')
        contactnum = request.GET.get('contactnum')
        attachment_url = request.GET.get('attachment_url')

        # Pass the parameters to the template
        return render(request, 'members/check_info.html', {
            'id_number': id_number,
            'name': name,
            'address': address,
            'contactnum': contactnum,
            'attachment_url': attachment_url
        })

# from django.shortcuts import render
# from .models import ServiceRequest

from .models import Request
from django.shortcuts import render, get_object_or_404
# from .models import ServiceRequest

# from django.shortcuts import render, get_object_or_404




from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest

def check(request):
    if request.method == 'GET':
        # Get the name and id_number from the form submission
        name = request.GET.get('name')
        id_number = request.GET.get('id_number')

        try:
            # Query the database for the matching record
            service_request = ServiceRequest.objects.get(name=name, id_number=id_number)
            # If a matching record is found, pass its data to the template
            return render(request, 'members/check_info.html', {
                'id_number': service_request.id_number,
                'name': service_request.name,
                'address': service_request.address,
                'contactnum': service_request.contactnum,
                'attachment_url': service_request.attachment.url if service_request.attachment else None
            })
        except ServiceRequest.DoesNotExist:
            # If no matching record is found, handle it as desired
            error_message = "No matching record found."
            return render(request, 'members/check.html', {'error_message': error_message})

    # If the request method is not GET, render the check.html template
    return render(request, 'members/check.html')





# from django.shortcuts import render
from .models import Request

def maker(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        name = request.POST.get('name')
        service_type = request.POST.get('service_type')
        status = request.POST.get('status')  # Getting the status from radio buttons

        new_request = Request.objects.create(
            id_number=id_number,
            name=name,
            service_type=service_type,
            status=status  # Saving the status
        )
        new_request.save()

        return render(request, 'members/maker.html')

    return render(request, 'members/maker.html')


# Other view functions...


# from django.shortcuts import render
# from .models import Request

def track_request(request):
    # Retrieve all request objects from the database
    all_requests = Request.objects.all()

    # Pass the request objects to the template for rendering
    return render(request, 'members/track_request.html', {'all_requests': all_requests})

# from django.shortcuts import render, redirect
# from .models import Request

def manage_request(request):
    if request.method == 'POST':
        id_number = request.POST['id_number']
        name = request.POST['name']
        # Query the database for the request to delete
        request_to_delete = Request.objects.filter(id_number=id_number, name=name)
        if request_to_delete.exists():
            # If the request exists, delete it
            request_to_delete.delete()
            return render(request, 'members/manage_request.html')  # Redirect back to the manage request page
        else:
            # If the request does not exist, display a message or handle the error as desired
            return render(request, 'members/manage_request.html', {'message': 'Request not found.'})
    else:
        return render(request, 'members/manage_request.html')

# from django.shortcuts import render
# from .models import Request

