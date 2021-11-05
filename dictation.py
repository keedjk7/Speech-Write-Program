from gtts import gTTS
from random import randrange

import os

list_text = ["Consciousness","historic properties","drought","epidemic","disaster","culture shock","commercial sex","impact of tourism industry","cultural diplomacy", "living expense","national identity","foreign exchange earning", "tour guide", "complex society", "literature", "Industrialization", "earthenware", "textile", "folk medicine", "cultural wisdom","culture", "tradition", "conventional custom", "moral custom", "believe", "faith", "sacred", "Chronological ritual", "International excursionist","sculpture", "architecture", "tourism resources" ,"tourism marketing", "verbal communication", "non-verbal communication", "facial expression" , "gesture", "etiquette", "contribution to government revenues" , "stimulation of infrastructure investment"]

language = 'en'

txt = list_text[randrange(40)]
print(txt)

myobj = gTTS(text=txt  ,lang=language , slow= True)

myobj.save("dication.mp3")

os.system("/Users/keedjk7/Documents/Work_And_Study/speech_write/dication.mp3")