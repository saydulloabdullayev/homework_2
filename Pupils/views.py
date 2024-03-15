from django.shortcuts import render

# Sample data of pupils
pupils = [
    {'id': 1, 'name': 'Muhammad Choriyev' ' -->25 Ball'},
    {'id': 2, 'name': 'Javlon Nosirov' ' -->20 Ball'},
    {'id': 3, 'name': 'Diyorbek Vafoqulov' ' -->23 Ball'},
    {'id': 4, 'name': 'Ravshanov To`lqin' ' -->25 Ball'},
    {'id': 5, 'name': 'Ahmad Mamasafoyev' ' -->28 Ball'},
    {'id': 6, 'name': 'Fazliddin Akmalov' ' -->22 Ball'},
]

def pupils_list(request):
    context = {'pupils': pupils}
    return render(request, 'Publis/pupil_list.html', context)

def pupil_detail(request, id):
    pupil = next((pupil for pupil in pupils if pupil['id'] == id), None)
    context = {'pupil': pupil}
    return render(request, 'Publis/pupil_detail.html', context)


