#Loops structures are used to repeat sections of code.
#They are useful if you have to do the same thing more than once
#or you can establish a pattern

#Example 1:
#This is counted loop. I want you to think about
#Count, check, change
#i = 0,0 < 5 TRUE - RUN LOOP
#i = 1,1 < 5 TRUE - RUN LOOP
#i = 2,2 < 5 TRUE - RUN LOOP
#i = 3,3 < 5 TRUE - RUN LOOP


for i in range(4,11,2):
	print(i)



print("----------[Backwards]------------")



for i in range(10,-1,-1):
	print(i)

print("-------------[Monkey]------------")

#INDICATE THE LENGTH OF WORD USING THE FUNCTION 
#len
str = "Monkey"

for i in range(5,-1,-1):
	print(str[i])
print("-----------[Print Every Second Letter in Str start at index 0]----------------")

for i in range(0,len(str),2):
	print(str[i])
		

