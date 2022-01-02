import random 
import re 
import time 

# Starting Variables 
CollegeCareers={
'Nurse':{'Job':'Nurse','Salary':80000},
'Doctor':{'Job':'Doctor','Salary':150000},
'Lawyer':{'Job':'Lawyer','Salary':120000},
'Judge':{'Job':'Judge','Salary':160000},
'Scientist':{'Job':'Scientist','Salary':130000},
'Computer Programmer':{'Job':'Computer Programmer','Salary':140000},
'CEO':{'Job':'CEO','Salary':1000000},
'Accountant':{'Job':'Accountant','Salary':100000},
'Teacher':{'Job':'Teacher','Salary':90000}
}
Careers={
'Mechanic':{'Job':'Mechanic','Salary':40000},
'Loan Collector':{'Job':'Loan Collector','Salary':30000},
'Dishwasher':{'Job':'Dishwasher','Salary':20000},
'Cook':{'Job':'Cook','Salary':50000},
'Uber Driver':{'Job':'Uber Driver','Salary':35000},
'Musician':{'Job':'Musician','Salary':19000},
'Bodyguard':{'Job':'Bodyguard','Salary':70000},
'Influencer':{'Job':'Influencer','Salary':200000},
'Reality TV Star':{'Job':'Reality TV Star','Salary':150000},
'Famous Actor':{'Job':'Famous Actor','Salary':1000000}
}

Players = {}

# Functions 
def playerchoice (question,parameters,errormsg):
	decision = ''
	toask = question
	while True:
		decision = input(toask)
		if re.match(parameters,decision):
			return decision 
			break
		print (errormsg)

def yesmatch (query):
	if re.match(r'Yes|yes|y|Yes.|Y',query):
		return True
	else:
		return False

def st(secs=0.5):
	time.sleep(secs)

def shuffle(fastness=0.2):
	for x in range(3):
		for frame in r'-\|/-\|/':
			# Back up one character then print our next frame in the animation
			print('\b', frame, sep='', end='', flush=True)
			st(fastness)

print ('*********  Welcome to the Python Game of Life!*********\n')
st()
NumPlayers = input ("How many people are playing today? ")
st()
print ('\nThanks!')
st()
print ('\nSo I just need to ask a few questions before we get started.\n')
st()
print ('')
count = 1
while count < int(NumPlayers) +1 :
	CurrentPlayer = str(count)
	PlayerSlot = 'Player '+ CurrentPlayer
	NamePrompt = 'What is Player '+str(count)+'\'s name? '
	PlayerName = input (NamePrompt)
	Players[PlayerSlot] = {'Name': PlayerName}
	PlayerCollege = playerchoice('Does ' + Players[PlayerSlot]['Name'] +' want to go to college? ',r'Yes|No|yes|no|y|n|Yes.|No.|Y|N','Please type either yes or no.')
	if yesmatch(PlayerCollege) == True:
		CareerSet = CollegeCareers
		Players[PlayerSlot].update({'College': 'Yes'})
	else:
		CareerSet = Careers
		Players[PlayerSlot].update({'College': 'No'})
	RandCareer = random.choice(list(CareerSet.values()))
	PickedCareer = RandCareer['Job']
	Players[PlayerSlot].update({'Career': PickedCareer})
	PSalary = CareerSet[PickedCareer]['Salary']
	Players[PlayerSlot].update({'Salary': PSalary})
	CareerSet.pop(PickedCareer)
	PlayerKidChoice = playerchoice('Does ' + Players[PlayerSlot]['Name'] + ' want to try to have kids? ',r'Yes|No|yes|no|y|n|Yes.|No.|Y|N','Please type either yes or no.')
	if yesmatch(PlayerKidChoice) == True:
		kids = random.randint(0,6)
	else:
		kidlottery = random.randint(1,10)
		if kidlottery > 9:
			kids = 2
		elif kidlottery > 7:
			kids = 1
		else:
			kids = 0
	Players[PlayerSlot].update({'Kids': kids})
	print ('Okay, thanks!\n')
	st()
	count +=1

print ('Okay, let me shuffle the career cards and deal them to the players\n')

shuffle()
print ('')

for i in Players:
	CPlayer = Players[i]
	salary = "${:,.0f}".format(CPlayer['Salary'])
	CPlayerCareer = CPlayer['Career']
	print (CPlayer['Name']+'\'s career is',CPlayerCareer,'and their salary is',salary)
	print ('')
	shuffle(0.1)
	print ('')
	st

print ('Now I will play the game!')
shuffle()
print('')

for i in Players:
	CPlayer = Players[i]
	if CPlayer['College'] == 'Yes':
		turns = 8
	else:
		turns = 10
	randfactor = random.randint(50000,500000)
	winnings = randfactor + (CPlayer['Salary']*turns)
	if CPlayer['Kids'] == 1:
		kids = 'kid'
	else:
		kids = 'kids'
	print (CPlayer['Name'],'ends the game with',"${:,.0f}".format(winnings),'and',CPlayer['Kids'],kids)
	CPlayer.update({'Winnings': winnings})
	print ('')
	shuffle(0.1)
	print('')
	st()
	
winningpot = 0
winner = ''
for i in Players:
	CPlayer = Players[i]
	if CPlayer['Winnings'] > winningpot:
		winningpot = CPlayer['Winnings']
		winner = CPlayer['Name']

print ('That means the winner is...\n')
shuffle(0.05)
print ('\n*****'+winner+'*****!')
print ('')
st()
print ('Thanks for playing the Pyhton Game of Life!\n')
print (Players)