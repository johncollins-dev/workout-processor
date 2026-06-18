'''
datatype_tests.py
Run: python tests/datatype_tests.py
'''
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from data.data import *

print("test file is running")
# muscles
lat = Muscle('Latissimus Dorsi')
biceps = Muscle('biceps')
rhomboids = Muscle('rhomboids')

# tags
bodyweight = Tag('#bodyweight')
hard = Tag('#hard')
pubar = Tag('#pullupbar')

# equipment
pull_up_bar = Equipment('Pull Up Bar')

# adaptation
strength= Adaptation('Strength')

# movement
vertical_pull = Movement('Vertical Pull')

# exercise
lat_pulldown = Exercise('Lat Pulldown')
oa_pull_up = Exercise('One Arm Pull Up')

'''
Testing Exercise
'''
exercise1 = Exercise('Push Up')
#print(repr(exercise1))
exercise1.demo = 'https://www.youtube.com/watch?v=WDIpL0pjun0'
#print(repr(exercise1))
exercise2 = Exercise(
        name='Pull Up',
        demo='https://www.youtube.com/watch?v=aAggnpPyR6E',
        prime_mover=lat,
        equipment=pull_up_bar,
        instructions='grip the bar and pull up',
        description='an effective strength exercise for the back',
        notes='pull the bar to your chest and pinch your scaps',
        progression=oa_pull_up,
        regression=lat_pulldown,
        adaptation=strength,
        movement=vertical_pull,
        synergists = [biceps, rhomboids],
        tags = [bodyweight, hard, pubar]
)
#print(repr(exercise2))

'''
Testing Line
'''
line1 = Line(
        exercise2,
        [Cell('Set 1', '6'),
         Cell('Set 2', '6'),
         Cell('Set 3', '6'),
         Cell('Set 4', '6'),
         Cell('Rest', '60s')]
)
#print(repr(line1))

'''
Testing Block
'''
block1 = Block(
        title='Strength'

)
print(repr(block1))
