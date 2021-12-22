from django.shortcuts import render
from django.http import *
from .models import Todolistitem
# from django.http import *


def todoappview(request):
    all_todo_items = Todolistitem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addtodoview(request):
     x = request.POST['content']
     new_item = Todolistitem(content = x)
     new_item.save()
     return HttpResponseRedirect('/create/')


def deletetodoview(request, i):
     y = Todolistitem.objects.filter(id = i).delete()

     return HttpResponseRedirect( '/create/')


# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
# def printParenthesis(str, n):
#     if (n > 0):
#         _printParenthesis(str, 0,
#                           n, 0, 0)
#     return
#
#
# def _printParenthesis(str, pos, n,
#                       open, close):
#     if (close == n):
#         for i in str:
#             print(i, end="")
#         print()
#         return
#     else:
#         if (open > close):
#             str[pos] = ')'
#             _printParenthesis(str, pos + 1, n,
#                               open, close + 1)
#         if (open < n):
#             str[pos] = '('
#             _printParenthesis(str, pos + 1, n,
#                               open + 1, close)
#
#
# # Driver Code
# n = 4
# str = [""] * 2 * n
# printParenthesis(str, n)
#
#
#
#
# str1 = input("Enter the Letters")
# c = str1.split()
# print(c)
# vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
# for i in str1:
#     print()
#     for j in vowels:
#         if str1 == vowels:
#             print(i)
#     print(i)
# a = []
# b = []
#
# if str1.split() == vowels:
#     print(a.append(str1))
# else:
#     print(b.append(str1))



# This Code is contributed
# by mits.
