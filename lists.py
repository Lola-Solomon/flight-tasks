if __name__ == '__main__':
    n = int(input())
    lst=[]
    for i in range (0,n):
        com=input().split();
        if com[0]=="insert":
            lst.insert(int(com[1]),int(com[2]))
        elif com[0]=="append":
            lst.append(int(com[1]))
        elif com[0]=="pop":
            lst.pop()
        elif com[0]=="sort":
            lst.sort()    
        elif com[0]=="remove":
            lst.remove(int(com[1]))          
        elif com[0]=="reverse":
            lst.reverse()
        else :
            print(lst)    
                  