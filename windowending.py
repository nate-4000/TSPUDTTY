from intro import pprint
import time
import sys
def ending():
    pprint("""
[You land in a very small amount of nothing. You look around. There is nothing.]

Do you:
1. Do nothing
2. Do nothing
> 
""")
    time.sleep(3)
    pprint("""
At first, Stanley assumed he had broken the text adventure, until he saw this narration and realized it was a part of the game's design all along.
He then praised the game for its insightful and witty commentary into the nature of video game structure and its examination of structural narrative tropes.

So now that you're here, what do you think? Isn't this a fun and unique place to be?
Why don't we take a minute just to drink it all in!
""")
    time.sleep(3)
    pprint("""
Okay, I'm over it. Here's the "end" part of your ending.

<THE WINDOW ENDING>
""")
    input()
    sys.exit(None)

if __name__ == "__main__":
    import serious