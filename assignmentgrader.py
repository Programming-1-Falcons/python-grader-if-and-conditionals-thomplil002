points_possible = float(input("Enter how many points are possible:"))
points_achieved = float(input("Enter how many points were achieved: "))


grade = (points_achieved / points_possible)

grade = (grade * 100)

round = ( grade , 4 )



#0 - 50% = F

#51% - 60% = D

#61% - 75% = C

#76% - 88% = B

#89% - 100% = A


if grade == (89.00) or grade > (89.00):
    print("A")
elif grade >= (76.00) and grade < (89.00):
    print ("B")
elif grade >= (61.00) and grade < (76.00):
    print ("C")
elif grade >= (51.00) and grade < (61.00):
    print("D")
elif grade >= (0.00) and grade < (51.00):
    print ("F")
else:
    print("Invalid input")