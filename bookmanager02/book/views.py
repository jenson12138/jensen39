from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpRequest
# Create your views here.
def index(request):
    # zeng shan gai cha
    books=BookInfo.objects.all()
    print(books)
    return HttpResponse('index')



##################         add data           ############3
from book.models import BookInfo
book=BookInfo(
    name='Django',
    pub_date='2010-1-1'
)
book.save()

#method 2
#objects ---like an agency
BookInfo.objects.create(
    name='test development',
    pub_date='2025-1-1'
)

##############  modify ############
#method 1
book=BookInfo.objects.get(
    id=6
)
book.name='DevOps'
#method 2
BookInfo.objects.filter(id=6).update(name='crawler', commentcount=666)

###############drop data#######
#method 1
book=BookInfo.objects.get(id=1)
# physical del(data recoring) and logic del(modify marking,like is_delete=False)
book.delete()
#
# #method 2
# BookInfo.objects.filter(id=5).delete()
#
#
# BookInfo.objects.create()
# BookInfo.objects.filter(id=1).update(name='')
# BookInfo.objects.filter(id=3).delete()


from book.models import PeopleInfo
PeopleInfo.objects.all()
BookInfo.objects.filter(id=1)
PeopleInfo.objects.get()

from book.models import BookInfo
BookInfo.objects.filter(name__contains='')