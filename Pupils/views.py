from django.shortcuts import render

# Sample data of pupils
pupils = [
    {'id': 1, 'name': 'Yusufjon Muhammadov' ' -->35 Ball'},
    {'id': 2, 'name': 'Nurbek Doniyorov' ' -->25 Ball'},
    {'id': 3, 'name': 'Boburmirzo Muhammadov' ' -->31 Ball'},
    {'id': 4, 'name': 'Fazliddin Asomov' ' -->35 Ball'},
    {'id': 5, 'name': 'Muhammadjon Ibrohimov' ' -->38 Ball'},
    {'id': 6, 'name': 'Umarjon Umarov' ' -->33 Ball'},
    {'id': 7, 'name': 'Asadbek O\'ralov' ' -->30 Ball'},
]

def pupils_list(request):
    context = {'pupils': pupils}
    return render(request, 'Publis/pupil_list.html', context)

def pupil_detail(request, id):
    pupil = next((pupil for pupil in pupils if pupil['id'] == id), None)
    context = {'pupil': pupil}
    return render(request, 'Publis/pupil_detail.html', context)
