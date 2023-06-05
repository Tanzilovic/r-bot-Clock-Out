import components
import subprocess
import time
import sys

print('Would you like me to assist you with your roundsys?')

answer = input()

if answer == 'y':

    amount = int(sys.argv[1])

    for roundsys in range(amount):
        components.roundsys.clockIn(roundsys)

    components.roundsys.write(roundsys)
    subprocess.run('clear')

elif answer == 'y -t':

    amount = int(sys.argv[1])

    for roundsys in range(amount):
        components.roundsys.clockOut(roundsys)

    components.roundsys.write(roundsys)
    subprocess.run('clear')

else:
    print('Sorry for bothering you...')
    time.sleep(0.5)