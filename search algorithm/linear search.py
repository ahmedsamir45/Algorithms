def Linear_Search(list1,item):
    for i in range(len(list1)):
        if (list1[i]==item):
            return 'exist and his index is :', i
    return 'not exist '

a=[1,3,5423,54,3563,54,3,54,345,3,54,3,54,3,54,34,54]
print(Linear_Search(a,54))