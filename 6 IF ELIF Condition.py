 # PROGRAM TO FIND GREATER BETWEEEN 3 NUMBERS

a=int(input("Enter your number A = "))
b=int(input("Enter your number B = "))
c=int(input("Enter your number C = "))

if  ((a>b) and (a>c)):
    print("A is greater")
elif ((b>a) and (b>c)):
    print("B is greater")
else :
    print("C is greater")

#-----------------------------------------------------------------------

  # PROGRAM TO TAKE THE INPUT OF 5 SUBJECT AND THEN ASSIGNING GRADE ACCORDINGLY

a=int(input("Enter the Marks of Subject 1 = "))
b=int(input("Enter the Marks of Subject 2 = "))
c=int(input("Enter the Marks of Subject 3 = "))
d=int(input("Enter the Marks of Subject 4 = "))
e=int(input("Enter the Marks of Subject 5 = "))
total= a+b+c+d+e
print("Your Total is = ",total)
per= total*0.2
print("Your Percentage is = ",per)
if (per<35):
    print("You have 'FAILED' !!!...")
elif ((per>=35) and (per<50)):
    print("Your grade is 'C'")
elif ((per>=35) and (per<50)):
    print("Your grade is 'C'")
elif ((per>=50) and (per<75)):
    print("Your grade is 'B'")
elif ((per>=75) and (per<90)):
    print("Your grade is 'A'")
else:
    print("Great !!.. You have 'A+' grade")

#-------------------------------------------------------------------------------
 # ACCORDING TO SHOPPING AMOUNT YOU WILL GET DISCOUNT THEN CALCULATE FINAL AMOUNT

amt=int(input("Enter the total Amount = "))
if (amt<1000):
    print("Opps !!... You don't have any Discount")
    print("Total amount to be paid is = ",amt)
elif ((amt>=1000) and (amt<5000)):
    print("Hurrayy!!.. You have 10% Discount")
    disc= amt * 0.1
    total_amt= amt-disc
    print("Total amount to be paid is = ",total_amt)
elif ((amt>=5000) and (amt<15000)):
    print("Hurrayy!!.. You have 20% Discount")
    disc= amt * 0.2
    total_amt= amt-disc
    print("Total amount to be paid is = ",total_amt)
elif ((amt>=15000) and (amt<30000)):
    print("Hurrayy!!.. You have 25% Discount")
    disc= amt * 0.25
    total_amt= amt-disc
    print("Total amount to be paid is = ",total_amt)
elif ((amt>=30000) and (amt<50000)):
    print("Hurrayy!!.. You have 45% Discount")
    disc= amt * 0.45
    total_amt= amt-disc
    print("Total amount to be paid is = ",total_amt)
else :
    print("Hurrayy!!.. You have 50% Discount")
    disc= amt * 0.5
    total_amt= amt-disc
    print("Total amount to be paid is = ",total_amt)

    

 
    
