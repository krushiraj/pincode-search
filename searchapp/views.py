from django.shortcuts import render
from searchapp.models import PincodeRecord

# Create your views here.
def index(request):
    if request.method == 'POST':
        query = request.POST['query']
        q_type = request.POST['q_type'] + '__icontains'
        records = PincodeRecord.objects.filter(**{q_type: query})
        return render(request, 'index.html', {'records': records})
    else:
        return render(request, 'index.html')