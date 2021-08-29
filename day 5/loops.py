heights=input("Enter height of students ").split()
sum=0
len1=0
for height in heights:
    sum+=int(height)
    len1+=1

avg=round(sum/len1,2)

print(f"Average height is {avg}")
