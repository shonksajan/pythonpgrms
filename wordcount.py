#sen = "Hello world"
#word_count = sen.count( " ") + 1
#print(word_count) 
#-------------------------------------------------------------------
#ini_str = "Hello world"
#sub_str = 'language'
#print(ini_str[7:14])
#n = len(ini_str)
#m = len(sub_str)
#print("Number of substrings:",count)
def count_substring(string, substring):
    count = 0
    sub_len = len(substring)
    str_len = len(string)
    for i in range(str_len - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count+1
string = "Hello ,hello ,hello!"
substring = "Hello"
print(count_substring(string, substring)) 

