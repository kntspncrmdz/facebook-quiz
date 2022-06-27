from itertools import count
from random import shuffle
from os import system

system('cls')

questions = [
    'Who is the founder of Facebook?',
    'Who is the first CFO of Facebook?',
    'On what year was Facebook founded?',
    'In what university did Facebook began?',
    'What is the new company name for Facebook, Inc.?',
    'What else did Mark Zuckerberg study, besides computer science, when he founded Facebook at Harvard University?',
    'What was Facebook called when it was launched on February 4, 2004?',
    'In what US state is Facebook\'s headquarters located?',
    'How old was Mark Zuckerberg when he founded Facebook?',
    'At least, how old is a person to use Facebook?'
]

score = 0
passing_score = len(questions) * 0.75

print('''---------------------------
 F A C E B O O K   Q U I Z
---------------------------

How much do you know about 
the famous social network
website, FACEBOOK?
''')
cont = input('Answer the quiz? y/n: ')
if cont == 'y':
    system('cls')
    while cont != 'n':
        questions_copy = questions.copy()
        shuffle(questions_copy)
        for i in range(len(questions_copy)):
            print(f'Question # {i+1}\n{questions_copy[i]}\n')
            correct_answer = ''
            if(questions_copy[i] == 'Who is the founder of Facebook?'):
                correct_answer == 'mark zuckerberg'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'mark zuckerberg':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is Mark Zuckerberg.\n')
            elif(questions_copy[i] == 'Who is the first CFO of Facebook?'):
                correct_answer == 'eduardo saverin'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'eduardo saverin':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is Eduardo Saverin.\n')
            elif(questions_copy[i] == 'On what year was Facebook founded?'):
                correct_answer == '2004'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == '2004':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is 2004.\n')
            elif(questions_copy[i] == 'In what university did Facebook began?'):
                correct_answer == 'harvard'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'harvard':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is Harvard.\n')
            elif(questions_copy[i] == 'What is the new company name for Facebook, Inc.?'):
                correct_answer == 'meta'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'meta':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is Meta.\n')
            elif(questions_copy[i] == 'What else did Mark Zuckerberg study, besides computer science, when he founded Facebook at Harvard University?'):
                correct_answer == 'psychology'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'psychology':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is psychology.\n')
            elif(questions_copy[i] == 'What was Facebook called when it was launched on February 4, 2004?'):
                correct_answer == 'thefacebook'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'thefacebook':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is Thefacebook.\n')
            elif(questions_copy[i] == 'In what US state is Facebook\'s headquarters located?'):
                correct_answer == 'california'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == 'california':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is California.\n')
            elif(questions_copy[i] == 'How old was Mark Zuckerberg when he founded Facebook?'):
                correct_answer == '19'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == '19':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is 19.\n')
            elif(questions_copy[i] == 'At least, how old is a person to use Facebook?'):
                correct_answer == '13'
                user_answer = input('Answer: ')
                user_answer = user_answer.lower()
                if user_answer == '13':
                    score = score + 1
                    print('Your answer is correct!\n')
                else:
                    score = score
                    print(f'Wrong answer. The correct answer is 19.\n')
        print(f'Your score is {score}/{len(questions_copy)}')
        if score >= passing_score:
            print('You passed the quiz\n')
        else:
            print('You failed the quiz\n')
        cont = input('Answer again? y/n: ')
        score = 0
        system('cls')
elif cont == 'n':
    print('Bye... See you next time :)')
else:
    print('Invalid input !!!!')
