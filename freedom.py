import intro
import random
pprint = intro.pprint
command = intro.command
diabnormal = [
"All of his co-workers were gone. What.. *ahem* ..ah, excuse me."
"How wonderful. Stanley was alone. Finally. This is great, he thought to himself. This is what I've wanted all along. I got what I wanted.",
"Stanley decided to go to the meeting room to check on his co-workers. He never functioned well by himself, and constantly needed support and guidance from others, so the thought of total solitude was terrifying to him.",
"All of his co-workers were... wait, no. This isn't the right office, is it? Is this Stanley's office?",
"'How long was I sitting there', Stanley wondered to himself. Minutes? Days? Centuries? Did something crucial happen while my senses were turned? He made a note to be more careful with time from now on.",
"A soft wind blew outside and perhaps rain started, and if it did it stopped shortly after. Stanley hoped that he would one day see weather.",
"Stanley this, Stanley that, Stanley this, Stanley that, Stanley this, Stanley that, Stanley this, Stanley that",
"Someone was following Stanley. He was sure of it. If he checked over his shoulder now, he would surely catch them. It was only a matter of time.",
"Even now, Stanley's office was a distant memory. What did it look like? There was a computer perhaps.. and a painting. Was it a painting, or a photo? He could no longer recall.",
"The meeting room, yes, that's where everyone would be. Stanley just needed to get to the meeting room and from then on he would never be alone ever again.",
"Just a step through this door, Stanley thought to himself, that's all I need. If I can make it through this door, I can make it through them all.",
"Already, this was uncomfortable, and Stanley decided that as soon as he found a new space he felt safe in, that he would never leave it again in his life.",
"Stanley had never seen the office this brightly lit. Was it a sign or something? He hoped it was. He hoped very much that it was.",
"\"I can't wait to tell this story to my co-workers\", Stanley thought. \"How amusing they'll find it! Oh, won't we all just laugh and laugh at the time I thought everyone had gone missing!\"",
"Stanley knew the office layout like the back of his hand. It was only a matter of time before he found the others, wherever they were. Just a matter of time."
]
def hallway0():
    if random.randint(0,50) > 45:
        pprint("All of his co-workers were gone. What could it mean?\nStanley decided to go to the meeting room; perhaps he had simply missed a memo.\n")
    else:
        pprint(random.choice(diabnormal) + "\n")
    pprint("""Do you:
1. Decide to climb on a desk
2. Try to open door 430, with a crowbar
3. Go into the next room
""")
    stdin = int(input("> "))
    if stdin == 1:
        pprint("""
[There is an open window near the desk you climbed on. It is big enough for you to fit.]

Do you:
1. Get off the desk
2. Climb out the window
""")
        stdin = int(input("> "))
        if stdin == 2:
            import windowending
            windowending.ending()
    if stdin == 2:
        pprint("""
Stanley? Why do you have a crowbar?
Where did you get that? And why are you trying to open door 430?
Here, I'll do it.
See? There's nothing trapped in here. Just that toaster and a microwave.
Oh, and the watermelon in the corner. Wait, what?
Ok, the more I look around, the more things appear. I'm closing the door, Stanley.
Alright... That was weird. Let's not do that again.
""")
    pprint("""
[You walk into the next room. There is nothing to interact with here.]
Do you:
1. Go into the next room
2. Do nothing, then go into the next room
""")
    stdin = int(input("> "))
    pprint("""
[This is a small hallway. Nothing to do here.]
Do you:
1. Go into the next room
2. Stare longingly at Employee 417's office
""")
    stdin = int(input("> "))
    if stdin == 2:
        pprint("""
Stanley, it's just another desk and monitor. Nothing special.
""")
    pprint("""
[You walk into the next room. It is a hallway. You are starting to get sick of hallway after hallway. 
Seriously, before this code snippet, hallway appears 6 times. 
You instictively walk into the next room, to be greeted with a fork in the path.]
When Stanley came to a set of 2 open doors, he entered the door on his left.
Do you:
1. Go through the left door
2. Go through the right door
""")
    stdin = int(input("> "))
    if stdin == 1:
        import leftdoor
        leftdoor.hallway1()
    if stdin == 2:
        import rightdoor
        rightdoor.hallway1()