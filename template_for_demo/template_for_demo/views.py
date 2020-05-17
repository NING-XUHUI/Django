from django.shortcuts import render


def index(request):
    context = {
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 100
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 119
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 129
            }, {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 189
            }
        ],
        'person': {
            'username': 'zhiliao',
            'age': 18,
            'height': 180
        },
        'comments':[
            '文章真好',
            '确实好'
        ]
    }
    return render(request, 'index.html', context=context)
