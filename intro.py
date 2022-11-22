import time
def pprint(st: int, u: int = 0.07) -> None:
    t = list(st)
    for i in t:
        print(i, end="", flush=True)
        time.sleep(u)
def command(prompt:str, max:int) -> int:
    while True:
        try:
            res = int(input(prompt))
            if not (1<=res<=max):
                print(f"Please enter an integer from 1 to {max}")
            else:
                return res
        except ValueError:
            print("Please enter an integer")
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
        pprint("""But Stanley simply couldn't handle the pressure.
What if he had to make a decision?
What if a crucial outcome fell under his responsibility?
He had never been trained for that!
No, this couldn't go any way except badly.
The thing to do now, Stanley thought to himself, is to wait.
Nothing will hurt me. Nothing will break me. In here, I can be happy, forever.
I will be happy.

Stanley waited.
Hours passed.
Then days.
Had years gone by?
He no longer had the ability to tell.

But the one thing he knew, for sure, beyond any doubt, was that if he waited long enough, the answers would come.
Eventually, some day, they would arrive. Soon, very soon now, this will end.
He will be spoken to. He will be told what to do.
Now it's just a little bit closer.
Now it's even closer. Here it comes..
""")
        pprint("<THE COWARD ENDING>")
        input()
        import sys
        sys.exit(None)
    import freedom
    freedom.hallway0()

if __name__ == "__main__":
    import serious
    
# Proofread
