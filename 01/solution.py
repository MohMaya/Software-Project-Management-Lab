# Write a program to find cyclometric complexity using 
#           PREDICATE NODE METHOD

f = open('sampleCode.cpp','r')
codes = f.readlines()

count=0
for line in codes:
    if("if" in line):
        count+=1
    if("for" in line):
        count+=1
    if("while" in line):
        count+=1
    if("switch" in line):
        count+=1

print("The Cyclomatic Complexity by Predicate Node method is : ",count+1)