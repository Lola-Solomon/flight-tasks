def merge_the_tools(string, k):
    # your code goes here
    lst = []
    lenn = 0
    for i in string:
        lenn += 1
        if i not in lst:
            lst.append(i)
        if lenn == k:
            print (''.join(lst))
            lst = []
            lenn = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)