from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project_name': 'Athletica Sportsware',
        'name': 'Ahmad Omar Mohammed Maknoon',
        'npm': '2406419612',
        'class': 'PBP D'
    }

    return render(request, 'main.html', context)
