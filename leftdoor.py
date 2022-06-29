from intro import pprint
slides = [
"How To Not Get Fired",
"Boss Appreciation Minute",
"Why The Projector Is Always Running",
"How Not To Save Power",
"How To Eat A Sandwich",
"Are We In A Simulation: The Proof"
]
import random
def hallway1():
    pprint("""
[You walk through a very long hallway. You are starting to wonder what a healthy hallway to office ratio is, and what said ratio would be for this office building.
You come upon the meeting room. The projector is running.]

Yet there was not a single person here either.
Feeling a wave of disbelief, Stanley decided to go up to his boss's office, hoping he might find an answer there.
Do you: 
1. Look at the projector screen
2. Go into the next room
""")
    stdin = int(input("> "))
    if stdin == 1:
        import time
        pprint("""
[The title of the presentation is """ + random.choice(slides) + ". You've seen this one before.]\n")
    pprint("""
[You walk into the next room. This room is another hallway, with a broom closet. The door does not seem to be locked.]

Do you:
1. Go in the broom closet
2. Go into the next room
""")
    stdin = int(input("> "))
    pprint("""
This path has not been finished yet. Please choose a different ending next time.

<THE UNFINISHED ENDING>
""")
    input()
    import sys
    sys.exit(0)