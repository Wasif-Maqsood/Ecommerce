from django.http import HttpResponse,JsonResponse

def home_page(request):
    print('home page requested')
    friends= ['hamid','amish','azan']
    return JsonResponse(friends,safe=False)