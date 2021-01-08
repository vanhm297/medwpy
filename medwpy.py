#ein Programm von vanhm
import time

print('Hallo friend. I am Python. What\'s your name? ')
yourName = input()
print()
print('Hi, ' + yourName + '. It\'s so nice to meet you.')
time.sleep(1)
print('I have heard that you are not doing so well these days.')
time.sleep(1)
print('You might feel a bit stressed, a bit anxious about what going on or things that not even happen yet')
time.sleep(1)
print('Or you might feel too tired of studying and working and people around you.')
time.sleep(1)
answer = ' '
while answer != 'yes' and answer != 'no':
    print('Is it true? (yes or no)')
    answer = input()

def Yes():
    print()
    time.sleep(1)
    print('''Alright. Let me help you.
It\'s just a simple practice.
You don\'t need anything but an open mind and an open heart.
You don\'t need a lot of time. Only 5 minutes. Is that okay? (press Enter or type anything)''')
    input()
    print()
    print('Good. Follow my lead and you will be fine.')
    print()
    time.sleep(4)
    print('''Let\'s begin with a nice comfortable seat.
Try to sit up nice and tall, best you can.
Relax your shoulder.
Relax your eyebrows.
Relax your whole body.
Forget those fucking things and really go into this moment, find our chills.''')
    time.sleep(12)
    
def meditate():
    print()
    time.sleep(2)
    print('Now start listen to your sound of breath.')
    time.sleep(2)
    print('With every exhale, allow your body to relieve all the negative emotions and thoughts.')
    print()
    breath = 0
    for breath in range(5):
        time.sleep(4)
        print('Take a deeeeeeeeeeeep breath.')
        time.sleep(4)
        print()
        print('Let it outttttttt')
        print()
        time.sleep(4)
    print('Now give yourself a smile. Appreciate yourself doing a VERY good job.')
    print()
    time.sleep(3)


#where my programm starts
if answer == 'yes':
    Yes()
    meditate()
    print('Do you feel calmer? (yes or no)')
    doAgain = input()
    while doAgain == 'no':
        print()
        print('That\'s fine. We can do it one more time.')
        meditate()
        print('Do you feel better? (yes or no)')
        doAgain = input()
    time.sleep(2)
    print()
    print('''Glad to know that :D.
Come to me any time you need a little chill, a little calm in your busy daily life.
It\'s time to shut down your computer, turn off your phone and go to bed.
Completely be ready for a new day.
Have a good sleep.
Python.''')
    input()
else:
    print()
    print('Oh, good for you. Bye then.')
    input()
