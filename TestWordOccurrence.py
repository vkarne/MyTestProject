# Content of a word occurrence

string_array = input("\nEnter array of string:")
word=input("\nEnter a word for check occurrence: ")
a = []
count = 0
a=string_array.split(" ")
for i in range(0,len(a)):
    if word == a[i]:
            count=count+1
print("\nCount of the word is: ", count)
