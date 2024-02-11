if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #we use map when we want to input integers with spaces 
    s=sorted(list(set(arr)))#converting map to sorted set array 
    b=s[len(s)-2]
    print(b)