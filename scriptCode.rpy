# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define larry = Character('Larry', color="#008000")
define mom = Character('Mom', color="#556b2f")
define kelvin = Character('Kelvin', color="#52ba48")


# The game starts here.

label start:

    image bedroom = "room.jpg"
    image baby = "Baby Crocodile cartoon Postcard.jpg"
    image kitchen = "kitchen.jpg"

    scene bedroom
    show baby

#first scene

    larry "Hi there! My name is Larry, and I am getting ready for a playdate, but I can't find my crocs anywhere! Can you help me find them?"
#choice yes

    menu bedroom:
        "Of course!":
            larry "I lost my three favorite gibits throughout the house. If I find them, they will help me find my crocs!"

#larry sad face
    larry "Let's start looking in my bedroom. Do you see one anywhere?"
#choice search room

    menu search:
        "Look under bed.":
            larry "Ahaaaa!"
        "Check drawers of dresser.":
            larry "Hmm not there."
            call search

    larry "There it is! Ah, now I remember. I left a gibit in the bathroom."
#leave room
    hide bedroom

    jump bathroom

#second scene
    label bathroom:
    show bathroom

    larry "Do you see it anywhere?"

    menu look:
        "Look in the tub.":
            larry "No luck here"
            call look
        "Check behind the toilet.":
            larry "Not here"
            call look
        "Open the mirror cabinet.":
            larry "You found it!"
            larry "Great job!"
            larry "Wait. What's that?"

#search bathroom
    menu select:
        "Pick up spatula":
            larry "Hey, this doesn't belong here. Let's bring this to Mom. I think she's in the kitchen."

#leave bathroom
    hide bathroom

    jump kitchen

#third scene
    label kitchen:
    show kitchen

    larry "Hi Mom! I found this in the bathroom."
    mom "Oh, thank you Larry! What are you up to, sweetheart?"
    larry "I am looking for the last gibit to my crocs. Have you seen it anywhere?"
    mom "Hmm... I thought I saw your little cousin, Kelvin, playing with it in the playroom. You should look there."
    larry "Okay, thanks Mom!"
#leave kitchen
    hide kitchen

    jump playroom

#fourth scene
    label playroom:
    show playroom

    larry "Hey Kelvin! Whatcha doing?"
    kelvin "Hi Larry. I'm making this super cool tower with these blocks!"
    show kelvintoys

    larry "That's awesome. Hey, have you seen my gibit anywhere? Mom said you were playing with it."
    kelvin "Oh yeah! I forgot to ask you. I borrowed your crocs and gibit because it was the perfect piece of treasure for my castle. Here you go!"
#receive crocs

    menu receive:
        "Pick up crocs":
            larry "So that's where they were. Thanks Kelvin!"

    hide playroom

#fifth scene
    scene bedroom
    show baby
    larry "Hooray! Now I have all my gibits and my crocs."
    larry "Looks like I'm ready for my playdate. Thanks for all your help!"

    return
