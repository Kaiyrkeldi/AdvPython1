#Kabken Kaiyrkeldi SE-2008
from itertools import permutations

def func():
    list_a = []
    a = int(input("Enter number of elements: "))
    i = 0
    for i in range(0, a):
        list_item = input()
        list_a.append(list_item)
    print(list(permutations(list_a)))
func()