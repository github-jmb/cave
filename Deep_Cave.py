"""This is the Deep Cave program by Al Sweigart from his Big Book of Small Python Projects."""

import random, sys, time

# Constants
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Press ctrl+c to stop')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
   # display tunnel segment
   rightWidth = WIDTH - gapWidth - leftWidth
   print('#' * leftWidth + ' ' * gapWidth + '#' * rightWidth)

   # check for ctrl + c
   try:
       time.sleep(PAUSE_AMOUNT)
   except KeyboardInterrupt:
       sys.exit

   # Adjust the left side width
   diceRoll = random.randint(1, 6)
   if diceRoll == 1 and leftWidth > 1:
       leftWidth -= 1
   elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
       leftWidth += 1
   else:
       pass

