#Kabken Kaiyrkeldi SE-2008

def func():
    list_a = []
    a = int(input("Enter number of elements: "))
    i = 0
    for i in range(0, a):
        list_item = input()
        list_a.append(list_item)
    res = permute(list_a)
    listToStr = ' '.join([str(elem) for elem in res])
    print("(" + listToStr + ")")
def permute(s):
    ch = list(s)
    if len(ch) == 2:
        per = ch[1] + ch[0] 
        return [''.join(ch)] + [per]
    if len(ch) < 2:
        return ch
    else:
        return [ init+per for init in ch for per in permute(''.join(ch).replace(init,""))] 
if __name__ == '__main__':
    func()