def minion_game(string):
    # your code goes here
    vowels = "AaEeIiOoUu"
    l=len(string) #length of the string
    kev=0 #kevin score
    stuart=0 #stuart score
    #searching for vowls in string 
    for i in range(l):
        #if the letter is vowl so it can make substrings
        #equal to (the length - index of string)
        if string[i] in vowels:
            kev += (l-i)
        else:
            stuart += (l-i)    
    if kev > stuart:
        print ("Kevin", kev)
    elif kev < stuart:
        print ("Stuart", stuart)
    else:
        print( "Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)