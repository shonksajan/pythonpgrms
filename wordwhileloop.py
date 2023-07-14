def sub(Stringt,subtr):
    count =0
    x = 0
    i = 0
    while i < len(Stringt):
        if Stringt[i] == " "or i== len(Stringt)-1:
            if i == len(Stringt)-1:
                i=i+1
            word =Stringt[x:i]
            print(word)
            x=i+1
            if word == subtr:
                count += 1
        i = i+1
    print(count)       
strt = input("Enter the string: ")
subtr = input("Enter the substring:")
sub(strt,subtr)