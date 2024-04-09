# -----------------------------------
# ------------Strings ---------------
# -----------------------------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Doubles Quotes"

myStringThree = 'This is Single Quote "Test" ' 
myStringFour = "This is Doubles Quotes 'Test' "

print(myStringOne) # Result => This is Single Quote
print(myStringTwo) # Result => This is Doubles Quotes
print(myStringThree) # Result => This is Single Quote "Test"
print(myStringFour) # Result => This is Doubles Quotes 'Test' 

myStringFive = """ First
Second "Test" 'Test' 
Third """ 
print(myStringFive) # Result => Second "Test" 'Test' 
#                     Third 
#                     First

myStringSix = ''' First
Second 'Test' "Test"
Third  '''
print(myStringSix) # Result =>  First
#                     Second 'Test' "Test"
#                       Third  
