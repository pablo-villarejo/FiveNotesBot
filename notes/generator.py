import random

# INSTRUMENTS = ["piano", "guitarra", "voz", "trompeta"]
INSTRUMENTS = ["piano"]
NOTES = ["C", "D", "E", "F", "G", "A", "B"]
OCTAVES = [3, 4, 5]

def get_random_instrument():
    return random.choice(INSTRUMENTS)

def get_random_notes(n=5):
    return [random.choice(NOTES) + str(random.choice(OCTAVES)) for _ in range(n)]
