str1=input()
str2=input()
loc=str2[-1]
c=0
for i in str1:
  if(i==loc):
    c+=1
print(c)
