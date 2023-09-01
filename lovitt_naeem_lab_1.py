'''
Created on Oct 17, 2022
Program acts a Voter demonstration application
@author: Naeem Lovitt
SDEV 300 7381
'''
import sys #pylint preferred this to exit()

#methods for validating user input
def forward (question):
    '''Method forward validates answers to questions, true,false, or invalid'''
    while True:
        answer = input(question).lower()
        if answer in ('y','yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Invalid answer!")
def cancel (decision):
    '''Method cancel exits program based on user input to question equal to false'''
    if decision is False:
        sys.exit(0)

#Variables, question constant, question list, and state list for validation
REGIS_Q = 'Do you want to continue with the voter registration? '

questions = ['What is your first name? ', 'What is your last name? ',
             'What is your age? ', 'Are you a U.S. CITIZEN? ',
             'What state do you live? ', 'What is your zipcode? ']

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


print(f'{"":*^50}') #formatted star top border
print('Welcome to the Voter registration Application.')


cancel(forward(REGIS_Q))#exits program if user wants to leave

#variable to for names
F_NAME = str(input(questions[0])).capitalize() #asks first question in list, capitalize input
while F_NAME in (""," "): #validates input is not an empty or blank string
    print('Field cannot be empty!')
    F_NAME = str(input(questions[0])).capitalize()
cancel(forward(REGIS_Q))


L_NAME = str(input(questions[1])).capitalize() #same as above
while L_NAME in (""," "):
    print('Field cannot be empty!')
    L_NAME = str(input(questions[0])).capitalize()
cancel(forward(REGIS_Q))#exits program if user wants to leave

#age
age = int(input(questions[2])) #third question in list
while age <= 0 or age >= 120: # cannot continue if not between these age ranges
    print("Invalid age input, try again!")
    age = int(input(questions[2]))

if age < 18: #user is booted out if too young
    print('Sorry, voters must be 18 or above to proceed.')
    sys.exit(0)
cancel(forward(REGIS_Q))


CITIZEN = forward(questions[3])
if CITIZEN is False: #user is booted out if not US citizen
    print('Sorry, you must be a U.S. CITIZEN to proceed further.')
    sys.exit(0)
cancel(forward(REGIS_Q))


STATE = input(questions[4]).upper()
while STATE not in states:#if input not in state list, user is asked again
    print('Sorry invalid input, try again!')
    STATE = input(questions[4]).upper()
cancel(forward(REGIS_Q))

zipcode = int(input(questions[5]))#zip code

#final output
print(f'\nThanks for registering to vote. Here is the information we received:\n\
Name (first, last): {F_NAME} {L_NAME}\n\
Age: {age}\n\
U.S. CITIZEN: {CITIZEN}\n\
State: {STATE}\n\
Zipcode: {zipcode}\n\
\nThanks for trying the Voter registration Application.\n\
Your voter registration card should be shipped within 3 weeks.')

print(f'{"":*^50}') #closing star border
