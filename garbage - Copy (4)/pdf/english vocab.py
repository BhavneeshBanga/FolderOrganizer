#UPDATED

import time
from plyer import notification
import random

list = [
    "Gratification: Satisfaction or pleasure gained from something.",
    "Leisure: Free time when one is not working and can relax or enjoy activities.", 
    "Chasing: Running after someone or something in order to catch or reach them.",
    "Ephemeral: Lasting for a very short time",
    "Serendipity: Finding something good without looking for it", 
    "Ubiquitous : Present everywhere at the same time",
    "Esoteric : Understood by only a small group of people",
    "Resilient : Able to recover quickly from difficulties.",
    "Juxtaposition : Placing two things side by side for contrast",
    "Euphoria : A feeling of extreme happiness",
    "Quintessential : The perfect example of something",
    "Inevitable : Certain to happen; unavoidable",
    "Zealous : Showing great energy or enthusiasm for something.",
    "Overwhelmed: Feeling extremely emotional, stressed, or overloaded with too many things at once",
    "Laborious : needing a lot of time & efforts",
    "Invariably : almost always",
    "Naturalist : a perso who studies plants and animals",
    "widow : a woman whose husband has died and who has not married again",
    "Indefatigable : never giving up or getting tired of doing something", 
    "obsecure : not well known",
    "Persuade : to make somebody to do something by giving him good reasons",
    "hastened : to be quick to do or say something ",
    "Chauffeur: A person hired to drive a private car for someone, usually a rich or important person.",
    "Paleontologists: Scientists who study fossils and ancient life forms to understand the history of life on Earth.",
    "Grunts: Short, low sounds made by a person or animal, often showing effort, discomfort, or anger.",
    "Groans: Deep sounds made when someone is in pain, annoyed, or complaining.",
    "Preoccupied: Lost in thought or distracted by something, so not paying attention to what's happening around.",
    "Heirloom: A valuable object (like jewelry or furniture) passed down from one generation to another in a family.",
    "Lullaby: A gentle song sung to help a baby or young child fall asleep."

]

while True:
    a = random.choice(list)
    for j in range(1):
        notification.notify(title = "REMINDER",message=a,timeout=30)
        time.sleep(180)
