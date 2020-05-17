from django.shortcuts import render


class Person:
    def __init__(self, username):
        self.username = username


def index(request):
    # p = Person("zhangsan")
    # context = {
    #     'person': p
    # }
    context = {
        'persons': [
            '鲁班一号',
            '阿克',
            '牛逼'
        ]
    }
    return render(request, 'index.html', context=context)
