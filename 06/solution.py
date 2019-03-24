# Write a program to implement
#      DETAILED COCOMO



kLOC = int(input("Enter the Number of Lines of Code (in kLOC)   :   "))



print("-------------------PRODUCT ATTRIBUTES--------------------")
print("a. Required Software Reliability \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
RSR=0
if(choice==1):
    RSR=0.75
elif(choice==2):
    RSR=0.88
elif(choice==3):
    RSR=1.00
elif(choice==4):
    RSR=1.15
elif(choice==5):
    RSR=1.40
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


print("b. Size of Application Database \n1. Low\n2. Nominal\n3. High\n4. Very High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
SoAD=0
if(choice==1):
    SoAD=0.94
elif(choice==2):
    SoAD=1.00
elif(choice==3):
    SoAD=1.08
elif(choice==4):
    SoAD=1.16
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


print("c. Complexity of the Product \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High\n6. Extra High")
choice = int(input("Enter Choice [1,2,3,4,5,6]  :   "))
CotP=0
if(choice==1):
    CotP=0.70
elif(choice==2):
    CotP=0.85
elif(choice==3):
    CotP=1.00
elif(choice==4):
    CotP=1.15
elif(choice==5):
    CotP=1.30
elif(choice==6):
    CotP=1.65
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit




print("\n\n-------------------HARDWARE ATTRIBUTES--------------------")
print("a. Run-time performance constraint \n1. Nominal\n2. High\n3. Very High\n4. Extra High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
RtPC=0
if(choice==1):
    RtPC=1.00
elif(choice==2):
    RtPC=1.11
elif(choice==3):
    RtPC=1.30
elif(choice==4):
    RtPC=1.66
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("b. Memory constraint \n1. Nominal\n2. High\n3. Very High\n4. Extra High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
MC=0
if(choice==1):
    MC=1.00
elif(choice==2):
    MC=1.06
elif(choice==3):
    MC=1.21
elif(choice==4):
    MC=1.56
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("c. Volatility of the Virtual Machine Environment \n1. Low\n2. Nominal\n3. High\n4. Very High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
VotVME=0
if(choice==1):
    VotVME=0.87
elif(choice==2):
    VotVME=1.00
elif(choice==3):
    VotVME=1.15
elif(choice==4):
    VotVME=1.30
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


print("d. Required Turnabout Time \n1. Low\n2. Nominal\n3. High\n4. Very High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
RTT=0
if(choice==1):
    RTT=0.87
elif(choice==2):
    RTT=1.00
elif(choice==3):
    RTT=1.07
elif(choice==4):
    RTT=1.15
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


print("\n\n-------------------PERSONNEL ATTRIBUTES--------------------")
print("a. Analyst Capability \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
AC=0
if(choice==1):
    AC=1.46
elif(choice==2):
    AC=1.19
elif(choice==3):
    AC=1.00
elif(choice==4):
    AC=0.86
elif(choice==5):
    AC=0.71
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("b. Software Engineer Capability \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
SEC=0
if(choice==1):
    SEC=1.29
elif(choice==2):
    SEC=1.13
elif(choice==3):
    SEC=1.00
elif(choice==4):
    SEC=0.91
elif(choice==5):
    SEC=0.82
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("c. Applications Experience \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
AE=0
if(choice==1):
    AE=1.42
elif(choice==2):
    AE=1.17
elif(choice==3):
    AE=1.00
elif(choice==4):
    AE=0.86
elif(choice==5):
    AE=0.70
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("d. Virtual Machine Experience \n1. Very low\n2. Low\n3. Nominal\n4. High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
VME=0
if(choice==1):
    VME=1.21
elif(choice==2):
    VME=1.10
elif(choice==3):
    VME=1.00
elif(choice==4):
    VME=0.90
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("e. Programming Language Experience \n1. Very low\n2. Low\n3. Nominal\n4. High")
choice = int(input("Enter Choice [1,2,3,4]  :   "))
PLE=0
if(choice==1):
    PLE=1.14
elif(choice==2):
    PLE=1.07
elif(choice==3):
    PLE=1.00
elif(choice==4):
    PLE=0.95
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("\n\n-------------------PROJECT ATTRIBUTES--------------------")
print("a. Use of Software Tools \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
UoST=0
if(choice==1):
    UoST=1.24
elif(choice==2):
    UoST=1.10
elif(choice==3):
    UoST=1.00
elif(choice==4):
    UoST=0.91
elif(choice==5):
    UoST=0.82
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


print("b. Application of Software Engg. Methods \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
AoSEM=0
if(choice==1):
    AoSEM=1.24
elif(choice==2):
    AoSEM=1.10
elif(choice==3):
    AoSEM=1.00
elif(choice==4):
    AoSEM=0.91
elif(choice==5):
    AoSEM=0.83
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("c. Required Development Schedule \n1. Very low\n2. Low\n3. Nominal\n4. High\n5. Very High")
choice = int(input("Enter Choice [1,2,3,4,5]  :   "))
RDS=0
if(choice==1):
    RDS=1.23
elif(choice==2):
    RDS=1.08
elif(choice==3):
    RDS=1.00
elif(choice==4):
    RDS=1.04
elif(choice==5):
    RDS=1.10
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit



print("\nEnter The BOEHM's Definition that fits your project : \n1. Oragnic\n2. Semi-Detached\n3. Embedded\n")
boehmCat = int(input("Enter your choice [1,2 or 3]  :   "))

a=0
b=0
c=0
d=0

if(boehmCat==1):
    a=3.20
    b=1.05
    c=2.5
    d=0.38
elif(boehmCat==2):
    a=3.0
    b=1.12
    c=2.5
    d=0.35
elif(boehmCat==3):
    a=2.8
    b=1.20
    c=2.5
    d=0.32
else:
    print("\nInvalid Choice. Exiting the program.\n")
    exit


#Effort Adjustment Factor
EAF = RSR*SoAD*CotP*RtPC*MC*VotVME*RTT*AC*SEC*AE*VME*PLE*UoST*AoSEM*RDS
print("Effort Adjustment Factor = ",EAF)
effort = a*(kLOC**b)*EAF
dev_time = c*(effort**d)
print("\nBy The Intermediate COCOMO : \nEffort = ",effort," Person-Months\nDevelopment time = ",dev_time," Chronological Months.")


print("************************STARTING DETAILED COCOMO*************************")
mode_code_size = ['Organic Small [S=2]', 'Organic Medium [S=32]', 'Semi-Detached Medium [S=32]', 'Semi-Detached Large [S=128]', 'Embedded Large [S=128]', 'Embedded XL [S=320]']
life_cycle_phases = ['Planning And Requirement', 'System Design', 'Detail Design', 'Code & Test', 'Integration & Test']
Up = [[0.06,0.16,0.26,0.42,0.16],[0.06,0.16,0.24,0.38,0.22],[0.07,0.17,0.25,0.33,0.25],[0.07,0.17,0.24,0.31,0.28],[0.08,0.18,0.25,0.26,0.31],[0.08,0.18,0.24,0.24,0.34]]
Tp = [[0.10,0.19,0.24,0.39,0.18],[0.12,0.19,0.21,0.34,0.26],[0.20,0.26,0.21,0.27,0.26],[0.22,0.27,0.19,0.25,0.29],[0.36,0.36,0.18,0.18,0.28],[0.40,0.38,0.16,0.16,0.30]]
#SOURCE : 8:03 @    https://www.youtube.com/watch?v=ziHWHLCcHgY

category_of_project = 0
if(kLOC>=320):
    category_of_project=5
elif(kLOC>=128 and boehmCat==3):
    category_of_project=4
elif (kLOC>=128 and boehmCat==2):
    category_of_project=3
elif (kLOC>=32 and boehmCat==2):
    category_of_project=2
elif (kLOC>=32 and boehmCat==1):
    category_of_project=1
else:
    category_of_project=0

print("Based on the size of the project, it belongs to : ",mode_code_size[category_of_project])
print("Now Printing Phase Wise Effort and Time : ")
for i in range(5):
    print("\n\n------------------",life_cycle_phases[i]," Phase------------------")
    print("Effort : ",Up[category_of_project][i]*effort," Person-Months")
    print("DevTime: ",Tp[category_of_project][i]*dev_time," Chronological Months")

print("\n\n")