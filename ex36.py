# --coding: utf-8--

from sys import exit

def start():
    print "One day, you woke up and found youself on an island alone."
    print "You searched all over the island, and found nothing but a horse and some apples."
    print "Both you and the horse are hungry." \
          "You can kill and eat the horse or share the apples with it and ride it cross the sea."
    print "What are you going to do?"

    while True:
        answer = raw_input("> ")

        if answer.find("kill") != -1:
            dead("Sorry. The rest food was eaten up and you are strave to death.")
        elif answer.find("share") != -1:
            print "Both you and the horse escape from the island successfully. Good job!"
            castale()
        else:
            print "I don't know what you mean."


def castale():
    print "After you escaped from the island, you came to a castale."
    print "In the castale, There were enough food and water. And you live in it for a couple of days."
    print "During these days, your life seemed comfortable besides some strange feelings."
    print "In the daytime, you always felt someone stared at you somewhere. "
    print "You heard a little girl weeping in a low voice at midnight. Are you going to leave or not?"

    while True:
        answer = raw_input("> ")

        if answer.find("Yes") != -1 or answer.find("yes") != -1:
            dead("Your choice maybe right. The little girl that wept at midnight is a ghost.")
        elif answer.find("No") != -1 or answer.find("no") != -1:
            print "So you are brave and you decided to find out the truth."
            curiosity()
        else:
            print "I don't know what you mean."


def curiosity():
    print "Even you are scared, but you stay up until 0 o'clock and the sound of weeping appeared again."
    print "You can choose to follow the sound or go to bed?"

    while True:
        answer = raw_input("> ")
        if answer.find("follow") != -1:
            print "What a barve man! And What a mistake it is! The weeping is from a sound recorder."
            exit(0)
        elif answer.find("bed") != -1:
            dead("Haha, finally you are a coward, But maybe you are safe.")
        else:
            print "I don't know what you mean."


def dead(reason):
    print "%s" % reason
    exit(0)


start()
