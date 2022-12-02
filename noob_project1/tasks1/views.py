from django.shortcuts import HttpResponse
from datetime import datetime
# introduction
def hello_view(request):

    return HttpResponse("welcome to my first project (introduction/ - info)")

def introduction_view(request):

    return HttpResponse("\nhome/ - initial page \ntime/ - time now, \ntask/ - for solution of task bellow ")

def time_view(reuest):

    return HttpResponse(f"now: {datetime.now()}")

def task_view(request):

    dict_1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

    return HttpResponse(dict_1.items())