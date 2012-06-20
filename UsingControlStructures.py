
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


 

