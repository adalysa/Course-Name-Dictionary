#Adalysa Rosales
#Lab 2
#2/25/2021

CS101={'Room Number' : '3004' , 'Instructor': 'Haynes' , 'Time' : '8:00am'}
CS102={'Room Number' : '4501' , 'Instructor': 'Alvarado' , 'Time' : '9:00am'}
CS103={'Room Number' : '6755' , 'Instructor': 'Rich' , 'Time' : '10:00am'}
NT110={'Room Number' : '1244' , 'Instructor': 'Burke' , 'Time' : '11:00am'}
CM241={'Room Number' : '1411' , 'Instructor': 'Lee' , 'Time' : '1:00pm'}

course=input("Enter a course number: ")

if(course=='CS101'):
    print(CS101.items())
elif (course == 'CS102'):
    print(CS102.items())
elif (course == 'CS103'):
    print(CS103.items())
elif (course == 'NT110'):
    print(NT110.items())
elif (course == 'CM241'):
    print(CM241.items())
else:
    print('That is not a course.')