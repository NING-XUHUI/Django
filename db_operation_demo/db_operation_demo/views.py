from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(id,name,author) value(null,'三国演义','罗贯中')")
    # result = cursor.execute("select * from book")
    cursor.execute("select id,name,author from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')
