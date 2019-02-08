#number1
dictionary = {'fullName': 'Abdulazeez Shinkafi','ReasonsForAttendingAISaturday': 'be able to integrate AI in my code'}
#number2
print('my name is ' + dictionary['fullName'], 'and at the end of the cohortII, i want to' +
      dictionary['ReasonsForAttendingAISaturday'])
#number3
numbers = [1,2,3,4,5,6,7,8,9]
countOdd = 0
countEven = 0
for number in numbers:
    if (number % 2) > 0:
        countOdd = countOdd+1
    else:
        countEven = countEven+1

#number4
print('number of even numbers: ', countEven)
print('number of odd numbers: ', countOdd)
