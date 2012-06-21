#question 5
theInput = raw_input("Enter integer:")
theInput = int(theInput)
if theInput%2 == 0:
 print 'even'
    
else:
 print 'odd'
print "--------"


#question 6
primarySchoolAge = 4
legalVotingAge = 18
presidentialage = 40
officialretirementage = 60

personsAge = input("Enter an age:")
if personsAge <= primarySchoolAge:
    print "Too young"
elif personsAge >= legalVotingAge:
    print "Remember to vote"
elif personsAge >= presidentialage:
    print "Vote for me"
elif personsAge >= officialretirementage:
    print "Too old"

print"---------"

#question 7 using for
for i in range(40,-1,-1):
    if i%3 == 0:
        print i
print"solving question 7 using while loop"        

 #using while for question 7
i = 40
while i >= 0:
    i = i - 1
    if i%3 == 0:
        print i

 #question 8
print"---------"
for i in range(6,30,1):
    
 if i%2 != 0 and i%3 != 0 and i%5 !=0:
   print i

print "--------------"

#question 9
n = 0
while n >= 0:
  n = n + 1  

  if 79*n%97 == 1:
   print n
   break
    



