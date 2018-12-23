
#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    total_count = len(request.GET['text2'])

    word_d = {}

    for word in request.GET['text2']:
        if word not in word_d:
            word_d[word] = 1
        else:
            word_d[word] += 1
        sorted_d = sorted(word_d.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html', {'total_count': total_count, 'text2': request.GET['text2'], 'wd': word_d, 'sorted': sorted_d})


