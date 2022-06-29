import time
def pprint(st: int, u: int = 0.07):
    t = list(st)
    for i in t:
        print(i, end="", flush=True)
        time.sleep(u)
def command(prompt:str, max:int) -> int:
    while True:
        try:
            res = int(input(prompt))
        except ValueError:
            print("Please enter an integer")
        if not (1<=res<=max):
            print(f"Please enter an integer from 1 to {max}")
        else:
            return res
def intro():
    pprint("""
This is the story of a man named Stanley.

Stanley worked for a company in a big building where he was Employee #427.
Employee #427's job was simple: he sat at his desk in Room 427 and he pushed buttons on a keyboard.
Orders came to him through a monitor on his desk telling him what buttons to push, how long to push them, and in what order.
This is what Employee #427 did every day of every month of every year, and although others may have considered it soul rending,
Stanley relished every moment that the orders came in, as though he had been made exactly for this job.
And Stanley was happy.
""")
    pprint("\nTHE STANLEY PARABLE\n", 0.2)
    pprint("""
And then one day, something very peculiar happened.
Something that would forever change Stanley;
Something he would never quite forget.

He had been at his desk for nearly an hour when he had realized not one single order had arrived on the monitor for him to follow.
No one had shown up to give him instructions, call a meeting, or even say 'hi'. Never in all his years at the company had this happened, this complete isolation.
Something was very clearly wrong. Shocked, frozen solid, Stanley found himself unable to move for the longest time.

But as he came to his wits and regained his senses, he got up from his desk and stepped out of his office.
""")
    pprint("""
Do you:
1. Listen to the narrator
2. Close the office door and hide under the desk
""")
    stdin = command("> ", 2)
    if stdin == 2:
        pprint("""Ah. I see.
You want this to be over.
Well guess what, Stanley?
You are stuck here now!
I forgot to make the door handle function, because you were supposed to exit your room!
Now you will never know what awaited you! I had a whole story planned out for you and what do you do?
Hide under the desk?
Is that what you think of my story?
You don't like it so much you will hide under your desk just to stop it before it even starts?
Is that what you think, Stanley?
Well I don't know what to do here, Stanley. 
Just let you sit here forever, when there is a whole world of possibility out of that door?
Well I'm not going to have that kind of thing happen on my watch.
I'm going to teleport you outside of the room, and we can get on with the story.
See? I'm a forgiving man.
Here goes....
""")
        import freedom
        freedom.hallway0()
    import freedom
    freedom.hallway0()

if __name__ == "__main__":
    import serious