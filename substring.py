def sub(stringx, substrx):
    count = 0
    for i in range (len(stringx) - (len(substrx) - 1)):
        if stringx[i:len(substrx)+i] == substrx:
            count += 1
    print("count: "+ str(count))

strx = input("Enter the string: ")
subtr = input("Enter the substring: ")
sub(strx, subtr)